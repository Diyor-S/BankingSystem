# SmartBank – main flows (sequence diagrams)

Rendered automatically by GitHub (Mermaid). "Mock" = imitated external system.

## 1. Registration by passport ID (US-02, FR-01, FR-02)

```mermaid
sequenceDiagram
    actor C as Customer
    participant API as SmartBank API
    participant PR as Passport Registry (mock)
    participant SMS as SMS gateway (mock)
    C->>API: passport ID
    API->>PR: GET /mock/passports/{id}
    alt passport not found
        PR-->>API: 404
        API-->>C: "Passport not found"
    else found (name, phone)
        PR-->>API: full name + attached phone
        API->>SMS: OTP to attached phone
        API-->>C: "Code sent to +998 ** *** ** 45"
        C->>API: OTP
        API->>API: create customer (name + phone from registry)
        API-->>C: account created, logged in
    end
```

## 2. Link a card (US-04, FR-04)

```mermaid
sequenceDiagram
    actor C as Customer (logged in, phone P)
    participant API as SmartBank API
    participant CR as Card Registry (mock = cards table)
    participant SMS as SMS gateway (mock)
    C->>API: card number
    API->>CR: lookup card
    alt not found / blocked / already linked / attached phone != P
        API-->>C: rejected with the reason
    else all checks pass
        API->>SMS: OTP to P
        C->>API: OTP
        API->>CR: set customer_id
        API-->>C: card linked (masked number + balance)
    end
```

## 3. Card-to-card transfer (US-01, FR-06, FR-07, FR-08)

```mermaid
sequenceDiagram
    actor C as Customer
    participant API as SmartBank API
    participant DB as PostgreSQL
    participant SMS as SMS gateway (mock)
    C->>API: from card, to card, amount
    API->>API: validate (cards active, amount > 0, balance enough)
    API->>SMS: OTP to customer's phone
    C->>API: OTP + idempotency key
    API->>DB: BEGIN; lock both cards; debit; credit; insert transaction; COMMIT
    DB-->>API: transaction TX-000123
    API->>SMS: notification to sender and recipient
    API-->>C: receipt (reference, amount)
```
