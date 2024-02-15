CREATE TABLE sessions (
    session_id UUID PRIMARY KEY,
    account_id INT NOT NULL REFERENCES accounts(account_id),
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    expires_at TIMESTAMP NOT NULL DEFAULT (NOW() + INTERVAL '1 day'),
    data JSON
);
