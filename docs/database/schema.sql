-- SmartBank (SB-2026) – PostgreSQL 16 schema
-- Run:  psql -d smartbank -f schema.sql && psql -d smartbank -f seed.sql && psql -d smartbank -f transfer_function.sql

CREATE SCHEMA IF NOT EXISTS mock;

-- ============================================================
-- MOCK EXTERNAL SYSTEMS (imitate systems we cannot access)
-- ============================================================

-- Mock Passport Registry (imitates the national citizen / passport database)
CREATE TABLE mock.passports (
    passport_id  VARCHAR(9)  PRIMARY KEY CHECK (passport_id ~ '^[A-Z]{2}[0-9]{7}$'),
    full_name    TEXT        NOT NULL,
    birth_date   DATE        NOT NULL,
    phone        VARCHAR(13) NOT NULL CHECK (phone ~ '^\+998[0-9]{9}$')   -- phone attached to the passport
);

-- Mock SMS gateway (stores every "sent" message; OTP codes are read here during demos)
CREATE TABLE mock.sms_messages (
    id          BIGSERIAL   PRIMARY KEY,
    phone       VARCHAR(13) NOT NULL,
    purpose     TEXT        NOT NULL,            -- register / login / link_card / transfer / unlink_card / notification
    body        TEXT        NOT NULL,
    delivered   BOOLEAN     NOT NULL DEFAULT TRUE,  -- set to FALSE to test gateway failures
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- ============================================================
-- SMARTBANK TABLES (T-03: 6 tables)
-- ============================================================

CREATE TABLE customers (
    id          BIGSERIAL   PRIMARY KEY,
    passport_id VARCHAR(9)  NOT NULL UNIQUE,                 -- one account per passport (FR-01)
    full_name   TEXT        NOT NULL,                        -- taken from the Passport Registry
    phone       VARCHAR(13) NOT NULL UNIQUE,                 -- taken from the Passport Registry
    status      TEXT        NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'frozen')),   -- FR-12
    consent_at  TIMESTAMPTZ NOT NULL DEFAULT now(),          -- consent to personal-data processing
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Cards of the bank. Seeded data = the mock Card Registry (card number -> attached phone, balance, status).
CREATE TABLE cards (
    card_number    CHAR(16)      PRIMARY KEY CHECK (card_number ~ '^[0-9]{16}$'),
    attached_phone VARCHAR(13)   NOT NULL,                                  -- phone attached to the card (FR-04)
    holder_name    TEXT          NOT NULL,
    balance        NUMERIC(18,2) NOT NULL DEFAULT 0 CHECK (balance >= 0),   -- never negative (NFR-06)
    currency       CHAR(3)       NOT NULL DEFAULT 'UZS',
    status         TEXT          NOT NULL DEFAULT 'active' CHECK (status IN ('active', 'blocked')),
    customer_id    BIGINT        REFERENCES customers(id)                   -- NULL until the card is linked
);
CREATE INDEX idx_cards_customer ON cards(customer_id);
CREATE INDEX idx_cards_phone    ON cards(attached_phone);

CREATE SEQUENCE tx_ref_seq START 1;

CREATE TABLE transactions (
    id              BIGSERIAL     PRIMARY KEY,
    reference       VARCHAR(20)   NOT NULL UNIQUE,            -- shown on the receipt, e.g. TX-000123
    idempotency_key VARCHAR(64)   NOT NULL UNIQUE,            -- duplicate protection (FR-08)
    from_card       CHAR(16)      NOT NULL REFERENCES cards(card_number),
    to_card         CHAR(16)      NOT NULL REFERENCES cards(card_number),
    amount          NUMERIC(18,2) NOT NULL CHECK (amount > 0),
    status          TEXT          NOT NULL DEFAULT 'completed' CHECK (status IN ('completed', 'failed')),
    created_at      TIMESTAMPTZ   NOT NULL DEFAULT now(),
    CHECK (from_card <> to_card)
);
CREATE INDEX idx_tx_from ON transactions(from_card, created_at DESC);
CREATE INDEX idx_tx_to   ON transactions(to_card,   created_at DESC);

CREATE TABLE otp_codes (
    id          BIGSERIAL   PRIMARY KEY,
    phone       VARCHAR(13) NOT NULL,
    purpose     TEXT        NOT NULL CHECK (purpose IN ('register', 'login', 'link_card', 'transfer', 'unlink_card')),
    code_hash   TEXT        NOT NULL,                          -- the code itself is never stored (NFR-03)
    expires_at  TIMESTAMPTZ NOT NULL,                          -- created_at + 3 minutes
    attempts    SMALLINT    NOT NULL DEFAULT 0 CHECK (attempts BETWEEN 0 AND 3),
    used        BOOLEAN     NOT NULL DEFAULT FALSE,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_otp_phone ON otp_codes(phone, purpose, created_at DESC);

CREATE TABLE admins (
    id            BIGSERIAL PRIMARY KEY,
    username      TEXT      NOT NULL UNIQUE,
    password_hash TEXT      NOT NULL,
    created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE audit_log (
    id          BIGSERIAL   PRIMARY KEY,
    actor_type  TEXT        NOT NULL CHECK (actor_type IN ('customer', 'admin', 'system')),
    actor_id    BIGINT,
    action      TEXT        NOT NULL,        -- e.g. VIEW_USER, FREEZE_ACCOUNT, LINK_CARD
    target_type TEXT,
    target_id   TEXT,
    details     JSONB,
    created_at  TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_audit_actor ON audit_log(actor_type, actor_id, created_at DESC);
