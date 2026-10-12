# SmartBank (SB-2026)

Digital banking system prototype: registration by passport ID, card linking (passport + phone + card must match) and OTP-confirmed card-to-card transfers.
Individual project of **Diyorxo'ja Saidaliyev**, group 319-24 – Practical Assignment 1, *Introduction to Software Engineering (ISWE)*.

External systems (national passport registry, card processing, SMS gateway) are **imitated by mock services with fictional test data**; no real money or real personal data is used.

## Documents

| What | Where |
|---|---|
| Full report (Tasks 0–6) | [docs/report/Saidaliyev_Assignment1.pdf](docs/report/Saidaliyev_Assignment1.pdf) |
| Life cycle diagram (Task 3.1) | [PNG](docs/diagrams/life-cycle.png) · [draw.io source](docs/diagrams/life-cycle.drawio) |
| Product Backlog, task cards, Sprint 1 plan (Task 4) | [docs/backlog-and-tasks.md](docs/backlog-and-tasks.md) |
| Draft wireframes (task T-02) | [docs/diagrams/wireframes.png](docs/diagrams/wireframes.png) |
| Use Case diagram (Task 5.2) | [PNG](docs/diagrams/use-case.png) · [PlantUML](docs/diagrams/use-case.puml) · [draw.io](docs/diagrams/use-case.drawio) |
| Technical Specification (Task 5.3) | [docs/technical-specification.md](docs/technical-specification.md) |
| Kick-off page (Task 6) | [docs/kickoff.md](docs/kickoff.md) |
| ER diagram | [docs/database/er-diagram.md](docs/database/er-diagram.md) |
| SQL schema, seed data, atomic transfer function | [docs/database/](docs/database) |
| Main flows (sequence diagrams) | [docs/flows.md](docs/flows.md) |
| REST API (OpenAPI) | [docs/api/openapi.yaml](docs/api/openapi.yaml) |

## Try the database (PostgreSQL 16)

```bash
createdb smartbank
psql -d smartbank -f docs/database/schema.sql
psql -d smartbank -f docs/database/seed.sql
psql -d smartbank -f docs/database/transfer_function.sql
psql -d smartbank -c "SELECT * FROM transfer_money('7000000000000001','7000000000000031',100000,'demo-key-1');"
```

Tested: 50 parallel transfers of 100 000 UZS from card `7000000000000001` (balance 1 000 000 UZS) give exactly 10 successes and 40 `INSUFFICIENT_FUNDS` errors, the balance ends at 0, and a repeated idempotency key returns the original transaction (no second debit).

## Test data (fictional)

| Cards | Purpose |
|---|---|
| `7000000000000001` – `…10` | linked to 5 seeded test customers (`…01` holds 1 000 000 UZS) |
| `…11` – `…20` | phone matches a passport – can be linked |
| `…21` – `…25` | attached phone differs from the holder's passport phone – linking must be rejected |
| `…26` – `…30` | blocked cards |
| `…31` – `…35` | active recipient cards |
| `…36` – `…40` | attached phone not found in the passport registry |

Passports `AA1000001`–`AA1000005` are already registered customers; `AA1000006`–`AA1000030` can register.
