-- SmartBank seed data: FICTIONAL test data only (no real people, no real cards)
BEGIN;

-- 30 fictional citizens in the mock Passport Registry
INSERT INTO mock.passports (passport_id, full_name, birth_date, phone) VALUES
  ('AA1000001', 'Sardor Saidov', '1978-02-06', '+998912000137'),
  ('AA1000002', 'Sevara Umarova', '1981-03-11', '+998932000274'),
  ('AA1000003', 'Javlon Ismoilov', '1984-04-16', '+998942000411'),
  ('AA1000004', 'Nargiza Nazarova', '1987-05-21', '+998972000548'),
  ('AA1000005', 'Aziz Normatov', '1990-06-26', '+998992000685'),
  ('AA1000006', 'Madina Sobirova', '1993-07-03', '+998882000822'),
  ('AA1000007', 'Rustam Abdullaev', '1996-08-08', '+998952000959'),
  ('AA1000008', 'Laylo Ergasheva', '1999-09-13', '+998902001096'),
  ('AA1000009', 'Nodir Tursunov', '2002-10-18', '+998912001233'),
  ('AA1000010', 'Malika Hasanova', '1975-11-23', '+998932001370'),
  ('AA1000011', 'Sardor Rakhimov', '1978-12-28', '+998942001507'),
  ('AA1000012', 'Sevara Mirzaeva', '1981-01-05', '+998972001644'),
  ('AA1000013', 'Javlon Yusupov', '1984-02-10', '+998992001781'),
  ('AA1000014', 'Nargiza Kodirova', '1987-03-15', '+998882001918'),
  ('AA1000015', 'Aziz Karimov', '1990-04-20', '+998952002055'),
  ('AA1000016', 'Madina Saidova', '1993-05-25', '+998902002192'),
  ('AA1000017', 'Rustam Umarov', '1996-06-02', '+998912002329'),
  ('AA1000018', 'Laylo Ismoilova', '1999-07-07', '+998932002466'),
  ('AA1000019', 'Nodir Nazarov', '2002-08-12', '+998942002603'),
  ('AA1000020', 'Malika Normatova', '1975-09-17', '+998972002740'),
  ('AA1000021', 'Sardor Sobirov', '1978-10-22', '+998992002877'),
  ('AA1000022', 'Sevara Abdullaeva', '1981-11-27', '+998882003014'),
  ('AA1000023', 'Javlon Ergashev', '1984-12-04', '+998952003151'),
  ('AA1000024', 'Nargiza Tursunova', '1987-01-09', '+998902003288'),
  ('AA1000025', 'Aziz Hasanov', '1990-02-14', '+998912003425'),
  ('AA1000026', 'Madina Rakhimova', '1993-03-19', '+998932003562'),
  ('AA1000027', 'Rustam Mirzaev', '1996-04-24', '+998942003699'),
  ('AA1000028', 'Laylo Yusupova', '1999-05-01', '+998972003836'),
  ('AA1000029', 'Nodir Kodirov', '2002-06-06', '+998992003973'),
  ('AA1000030', 'Malika Karimova', '1975-07-11', '+998882004110');

-- 5 already-registered test customers (passports 1-5): used in Sprint 1 with a temporary login
INSERT INTO customers (passport_id, full_name, phone) VALUES
  ('AA1000001', 'Sardor Saidov', '+998912000137'),
  ('AA1000002', 'Sevara Umarova', '+998932000274'),
  ('AA1000003', 'Javlon Ismoilov', '+998942000411'),
  ('AA1000004', 'Nargiza Nazarova', '+998972000548'),
  ('AA1000005', 'Aziz Normatov', '+998992000685');

-- 40 cards = mock Card Registry
--   cards 01-10: linked to the 5 test customers (card ...01 holds 1 000 000 UZS for the parallel-transfer test T-08)
--   cards 11-20: phone matches a passport, free to link          (positive linking test)
--   cards 21-25: attached phone differs from holder's passport    (linking must be rejected)
--   cards 26-30: blocked                                          (linking / transfer must be rejected)
--   cards 31-35: active recipients for transfers
--   cards 36-40: attached phone not found in the passport registry
INSERT INTO cards (card_number, attached_phone, holder_name, balance, status, customer_id) VALUES
  ('7000000000000001', '+998912000137', 'Sardor Saidov', 1000000.00, 'active', 1),
  ('7000000000000002', '+998912000137', 'Sardor Saidov', 1250000.00, 'active', 1),
  ('7000000000000003', '+998932000274', 'Sevara Umarova', 320000.00, 'active', 2),
  ('7000000000000004', '+998932000274', 'Sevara Umarova', 800000.00, 'active', 2),
  ('7000000000000005', '+998942000411', 'Javlon Ismoilov', 50000.00, 'active', 3),
  ('7000000000000006', '+998942000411', 'Javlon Ismoilov', 2000000.00, 'active', 3),
  ('7000000000000007', '+998972000548', 'Nargiza Nazarova', 150000.00, 'active', 4),
  ('7000000000000008', '+998972000548', 'Nargiza Nazarova', 600000.00, 'active', 4),
  ('7000000000000009', '+998992000685', 'Aziz Normatov', 90000.00, 'active', 5),
  ('7000000000000010', '+998992000685', 'Aziz Normatov', 3000000.00, 'active', 5),
  ('7000000000000011', '+998952000959', 'Rustam Abdullaev', 610000.00, 'active', NULL),
  ('7000000000000012', '+998902001096', 'Laylo Ergasheva', 620000.00, 'active', NULL),
  ('7000000000000013', '+998912001233', 'Nodir Tursunov', 630000.00, 'active', NULL),
  ('7000000000000014', '+998932001370', 'Malika Hasanova', 640000.00, 'active', NULL),
  ('7000000000000015', '+998942001507', 'Sardor Rakhimov', 650000.00, 'active', NULL),
  ('7000000000000016', '+998972001644', 'Sevara Mirzaeva', 660000.00, 'active', NULL),
  ('7000000000000017', '+998992001781', 'Javlon Yusupov', 670000.00, 'active', NULL),
  ('7000000000000018', '+998882001918', 'Nargiza Kodirova', 680000.00, 'active', NULL),
  ('7000000000000019', '+998952002055', 'Aziz Karimov', 690000.00, 'active', NULL),
  ('7000000000000020', '+998902002192', 'Madina Saidova', 700000.00, 'active', NULL),
  ('7000000000000021', '+998912003425', 'Madina Saidova', 400000.00, 'active', NULL),
  ('7000000000000022', '+998932003562', 'Rustam Umarov', 400000.00, 'active', NULL),
  ('7000000000000023', '+998942003699', 'Laylo Ismoilova', 400000.00, 'active', NULL),
  ('7000000000000024', '+998972003836', 'Nodir Nazarov', 400000.00, 'active', NULL),
  ('7000000000000025', '+998992003973', 'Malika Normatova', 400000.00, 'active', NULL),
  ('7000000000000026', '+998992002877', 'Sardor Sobirov', 100000.00, 'blocked', NULL),
  ('7000000000000027', '+998882003014', 'Sevara Abdullaeva', 100000.00, 'blocked', NULL),
  ('7000000000000028', '+998952003151', 'Javlon Ergashev', 100000.00, 'blocked', NULL),
  ('7000000000000029', '+998902003288', 'Nargiza Tursunova', 100000.00, 'blocked', NULL),
  ('7000000000000030', '+998912003425', 'Aziz Hasanov', 100000.00, 'blocked', NULL),
  ('7000000000000031', '+998932003562', 'Madina Rakhimova', 250000.00, 'active', NULL),
  ('7000000000000032', '+998942003699', 'Rustam Mirzaev', 250000.00, 'active', NULL),
  ('7000000000000033', '+998972003836', 'Laylo Yusupova', 250000.00, 'active', NULL),
  ('7000000000000034', '+998992003973', 'Nodir Kodirov', 250000.00, 'active', NULL),
  ('7000000000000035', '+998882004110', 'Malika Karimova', 250000.00, 'active', NULL),
  ('7000000000000036', '+998990000036', 'Unknown Holder 36', 75000.00, 'active', NULL),
  ('7000000000000037', '+998990000037', 'Unknown Holder 37', 75000.00, 'active', NULL),
  ('7000000000000038', '+998990000038', 'Unknown Holder 38', 75000.00, 'active', NULL),
  ('7000000000000039', '+998990000039', 'Unknown Holder 39', 75000.00, 'active', NULL),
  ('7000000000000040', '+998990000040', 'Unknown Holder 40', 75000.00, 'active', NULL);

-- Development-only admin; replace the hash with a real bcrypt/Argon2 hash generated by the backend
INSERT INTO admins (username, password_hash) VALUES ('admin', 'DEV-ONLY-REPLACE-WITH-HASH');

COMMIT;
