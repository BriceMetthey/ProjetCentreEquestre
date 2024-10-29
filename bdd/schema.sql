DROP TABLE IF EXISTS users;

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user' -- Peut être 'admin' ou 'user'
);



INSERT INTO users (username, email, password, role) VALUES ('admin', 'admin@exemple.com', 'admin_password', 'admin');
INSERT INTO users (username, email, password, role) VALUES ('user', 'user@exemple.com', 'user_password', 'user');
