CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    username VARCHAR(30) UNIQUE NOT NULL CHECK (char_length(username) >= 3),
    email_address VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    privileges INT DEFAULT 0,
    country VARCHAR(50) NOT NULL,
    wins: INT DEFAULT 0,
    loses: INT DEFAULT 0,
    draws: INT DEFAULT 0,
    win_rate: FLOAT DEFAULT 0,
    games_played INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

