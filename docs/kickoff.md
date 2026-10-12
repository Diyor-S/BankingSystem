# Kick-off: SmartBank

*Project SB-2026 · Diyorxo'ja Saidaliyev · group 319-24. This page is the single source of truth for the project: anyone who opens it should understand in 5 minutes what is being done and why.*

## Goal

The first version (MVP, pilot with 2,000 customers) must let a person register with a passport ID, link a card that matches their passport and phone, and make OTP-confirmed card-to-card transfers; it must give admins a monitoring panel and prove the effect with data: registration ≤ 2 minutes, at least 70 % of transfers made digitally, zero balance discrepancies, transfer time ≤ 3 s. **Sprint 1 goal:** a seeded test customer can see their cards and transfer money atomically and without duplicates.

## Stakeholders and their expectations

| **Stakeholder**              | **Expectation from the first version**                                                                                  |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Client (SmartBank JSC board) | A visible shift of simple operations from branches to digital, a demonstration for investors, controlled cost and risk. |
| Customers                    | Instant registration with a passport ID, safe transfers confirmed by OTP, clear information about every operation.      |
| Admins (bank staff)          | A simple view of all users, cards and transactions, the ability to freeze an account, a full audit trail.               |
| Marketer                     | A real working demo and screenshots to show; no promotion of features that do not exist yet.                            |
| Developer (the student)      | A clear specification, stable scope inside a Sprint, realistic deadlines, clear rules for mock data.                    |
| Regulator (indirect)         | Evidence of identity checks, audit trail and data protection if the system goes to real operation.                      |

## Scope and Out of Scope

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>In scope (MVP)</strong></th>
<th><strong>Out of scope (explicitly excluded)</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Registration by passport ID (mock Passport Registry) with OTP</p>
<p>Login with phone number and OTP</p>
<p>Linking a card with the passport–phone–card check</p>
<p>Viewing linked cards and balances</p>
<p>Card-to-card transfer confirmed by OTP</p>
<p>Transaction history</p>
<p>SMS notification for each transaction</p>
<p>Admin monitoring and account freezing</p>
<p>Mock Passport Registry, Card Registry and SMS gateway</p></td>
<td><p>Passport scanning with a camera, biometrics</p>
<p>Connection to real government and card-processing systems</p>
<p>Real money and real SMS sending</p>
<p>Bill payments, loans, international transfers</p>
<p>Native iOS / Android applications</p>
<p>Manual KYC review and fraud-analysis tools</p>
<p>All “features of competitors” that are not in the backlog</p>
<p>Paid advertising before the Sprint 1 demo</p></td>
</tr>
</tbody>
</table>

## Risks and assumptions

| **Risk**                                                                            | **Impact**                                | **Response plan**                                                                                                 |
|-------------------------------------------------------------------------------------|-------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| Scope creep: the client or the marketer asks for “everything at once”               | High – deadlines missed, poor quality     | MoSCoW priorities; changes only at Sprint Planning; Out-of-scope list confirmed by the client.                    |
| Mock registries are different from the real passport and card systems               | High – the integration later needs rework | Access only through adapters; data format agreed with the client; adapter tests; document differences.            |
| Money errors: double debit, lost transfer or negative balance                       | High – loss of money and trust            | Atomic transactions, idempotency keys, CHECK constraints; test T-08; NFR-06 measured before every release.        |
| OTP and account security weaknesses (guessing, repeated requests, theft of a phone) | High – unauthorised transfers             | Short OTP lifetime, attempt limits, rate limiting, hashing, masking, account freeze by an admin, OWASP ZAP scans. |
| Legal and regulatory duties not met in a real launch (licence, data law, AML/KYC)   | High – a real launch is blocked           | Prototype with test data only; consult a lawyer and the bank’s compliance officer before any real use.            |
| Personal capacity (one person: exams, illness)                                      | Medium – Sprint goal not reached          | 30 % buffer in every Sprint; strict MoSCoW – “Could” items are dropped first; weekly check of the plan.           |

**Assumptions:** (1) every person who registers has a passport record with a current phone number in the registry; (2) every card is attached to a phone number in the card registry; (3) customers have a smartphone and internet access and can receive SMS; (4) the baselines (1–2 days for onboarding, 45 % of transfers at branches) will be measured in the first pilot week; (5) the pilot uses test data and a mock SMS gateway until real services are connected.

## Communication plan

| **Event / report**             | **When**                       | **Participants and channel**                                | **Content**                                                           |
|--------------------------------|--------------------------------|-------------------------------------------------------------|-----------------------------------------------------------------------|
| Daily stand-up                 | Mon–Fri, 5-minute written note | Student; note in Trello / Notion log                        | Yesterday, today, blockers                                            |
| Sprint Planning                | First day of a Sprint, 2 h     | Student (Product Owner and Developer hats); written plan    | Sprint goal, tasks, capacity, risk review                             |
| Weekly meeting with the client | Friday, 30 min                 | Student and the client’s role-player; call or visit         | Progress, decisions, risks, questions                                 |
| Sprint Review (demo)           | Last day of a Sprint, 1 h      | Student, client’s role-player, one test user; call or visit | Demo of working software, backlog re-prioritisation                   |
| Retrospective                  | After the Review, 15 min       | Student; written note                                       | What to start, stop and continue                                      |
| Progress report to the client  | Every Friday                   | Student → client; e-mail                                    | One page: done, planned, risks, burndown screenshot, link to the demo |
| Documents and tasks            | Continuous                     | Student                                                     | GitHub (documents, code), Trello (tasks), Google Docs (kick-off page) |

## Success metrics

2,000 registered pilot customers in 3 months; registration ≤ 2 minutes; at least 70 % of their transfers made digitally; 0 balance discrepancies; transfer time ≤ 3 s (p95); availability ≥ 99.5 %; SUS ≥ 75; Sprint goal reached in each Sprint.
