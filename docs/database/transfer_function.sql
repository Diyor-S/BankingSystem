-- Atomic card-to-card transfer (US-01, FR-06, FR-08, NFR-06).  Task T-04 can call this function or
-- re-implement the same steps in the application code inside one DB transaction.
--
-- Error codes (map them to HTTP status in the API):
--   T0404 SENDER_CARD_NOT_FOUND / RECIPIENT_NOT_FOUND   -> 404
--   T0422 INSUFFICIENT_FUNDS                             -> 422
--   T0423 CARD_BLOCKED / ACCOUNT_FROZEN                  -> 423
--   22023 INVALID_AMOUNT / SAME_CARD                     -> 400
-- A repeated call with the same idempotency key returns the ORIGINAL transaction (no second debit).

CREATE OR REPLACE FUNCTION transfer_money(p_from CHAR(16), p_to CHAR(16), p_amount NUMERIC, p_key VARCHAR)
RETURNS transactions
LANGUAGE plpgsql AS $$
DECLARE
    v_from   cards;
    v_to     cards;
    v_tx     transactions;
    v_frozen BOOLEAN;
BEGIN
    IF p_amount IS NULL OR p_amount <= 0 THEN
        RAISE EXCEPTION 'INVALID_AMOUNT' USING ERRCODE = '22023';
    END IF;
    IF p_from = p_to THEN
        RAISE EXCEPTION 'SAME_CARD' USING ERRCODE = '22023';
    END IF;

    -- 1) idempotency: requests with the same key are serialised; the second one returns the first result
    PERFORM pg_advisory_xact_lock(hashtext(p_key));
    SELECT * INTO v_tx FROM transactions WHERE idempotency_key = p_key;
    IF FOUND THEN
        RETURN v_tx;
    END IF;

    -- 2) lock both cards in a fixed order (by card number) -> no deadlocks between opposite transfers
    PERFORM 1 FROM cards WHERE card_number IN (p_from, p_to) ORDER BY card_number FOR UPDATE;

    SELECT * INTO v_from FROM cards WHERE card_number = p_from;
    IF v_from.card_number IS NULL THEN
        RAISE EXCEPTION 'SENDER_CARD_NOT_FOUND' USING ERRCODE = 'T0404';
    END IF;
    SELECT * INTO v_to FROM cards WHERE card_number = p_to;
    IF v_to.card_number IS NULL THEN
        RAISE EXCEPTION 'RECIPIENT_NOT_FOUND' USING ERRCODE = 'T0404';
    END IF;

    -- 3) business checks
    IF v_from.status <> 'active' OR v_to.status <> 'active' THEN
        RAISE EXCEPTION 'CARD_BLOCKED' USING ERRCODE = 'T0423';
    END IF;
    IF v_from.customer_id IS NOT NULL THEN
        SELECT (status = 'frozen') INTO v_frozen FROM customers WHERE id = v_from.customer_id;
        IF v_frozen THEN
            RAISE EXCEPTION 'ACCOUNT_FROZEN' USING ERRCODE = 'T0423';
        END IF;
    END IF;
    IF v_from.balance < p_amount THEN
        RAISE EXCEPTION 'INSUFFICIENT_FUNDS' USING ERRCODE = 'T0422';
    END IF;

    -- 4) debit + credit + record, all in the caller's single transaction
    UPDATE cards SET balance = balance - p_amount WHERE card_number = p_from;
    UPDATE cards SET balance = balance + p_amount WHERE card_number = p_to;

    INSERT INTO transactions (reference, idempotency_key, from_card, to_card, amount, status)
    VALUES ('TX-' || lpad(nextval('tx_ref_seq')::text, 6, '0'), p_key, p_from, p_to, p_amount, 'completed')
    RETURNING * INTO v_tx;

    RETURN v_tx;
END;
$$;
