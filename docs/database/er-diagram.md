# SmartBank – ER diagram (task T-03)

Rendered automatically by GitHub (Mermaid). The SQL version is in [schema.sql](schema.sql).

Tables in the `mock` schema imitate external systems (Passport Registry, SMS gateway). The `cards` table is the bank's card table; its seeded data plays the role of the mock **Card Registry**.

```mermaid
erDiagram
    PASSPORTS ||--o| CUSTOMERS : "registration looks up (passport_id)"
    CUSTOMERS ||--o{ CARDS : "links (customer_id, NULL until linked)"
    CARDS ||--o{ TRANSACTIONS : "from_card"
    CARDS ||--o{ TRANSACTIONS : "to_card"
    CUSTOMERS ||--o{ OTP_CODES : "confirms by phone"
    ADMINS ||--o{ AUDIT_LOG : "actions"
    CUSTOMERS ||--o{ AUDIT_LOG : "actions"

    PASSPORTS {
        varchar passport_id PK "2 letters + 7 digits"
        text full_name
        date birth_date
        varchar phone "+998XXXXXXXXX"
    }
    SMS_MESSAGES {
        bigint id PK
        varchar phone
        text purpose
        text body
        boolean delivered
        timestamptz created_at
    }
    CUSTOMERS {
        bigint id PK
        varchar passport_id UK
        text full_name
        varchar phone UK
        text status "active / frozen"
        timestamptz consent_at
        timestamptz created_at
    }
    CARDS {
        char card_number PK "16 digits"
        varchar attached_phone
        text holder_name
        numeric balance "CHECK >= 0"
        char currency "UZS"
        text status "active / blocked"
        bigint customer_id FK "NULL until linked"
    }
    TRANSACTIONS {
        bigint id PK
        varchar reference UK "TX-000123"
        varchar idempotency_key UK
        char from_card FK
        char to_card FK
        numeric amount "CHECK > 0"
        text status
        timestamptz created_at
    }
    OTP_CODES {
        bigint id PK
        varchar phone
        text purpose
        text code_hash
        timestamptz expires_at "created_at + 3 min"
        smallint attempts "max 3"
        boolean used
    }
    ADMINS {
        bigint id PK
        text username UK
        text password_hash
    }
    AUDIT_LOG {
        bigint id PK
        text actor_type
        bigint actor_id
        text action
        text target_type
        text target_id
        jsonb details
        timestamptz created_at
    }
```
