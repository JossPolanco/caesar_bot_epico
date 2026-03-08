CREATE TABLE TBL_USERS(
        id SERIAL PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        active BOOLEAN DEFAULT TRUE
)

INSERT INTO tbl_users (id, username, password, active) VALUES (1, '5216145158918', '$2b$12$Y9MzgouNcqqQbaK7urDUyOr7SIfKEPNhEWQ7sky6K5FcFYH8nnvJC', true);
INSERT INTO tbl_users (id, username, password, active) VALUES (2, '5216146100739', '$2b$12$/oh3YYFu7mInKIZU9wf3P.qgOLRl5NtEJ0n0oolBDIMRnz3.rQUUu', true);
INSERT INTO tbl_users (id, username, password, active) VALUES (3, '5216144946274', '$2b$12$fXsGehcvpW4Hb0aCcFMPi.hqE0kmIJRF3kHlcfVDPomvigI1NlvYi', true);
