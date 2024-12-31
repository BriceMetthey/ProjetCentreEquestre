DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS statut;
DROP TABLE IF EXISTS cheval;


CREATE TABLE genre (
    genre_id INTEGER PRIMARY KEY AUTOINCREMENT,
    genre TEXT UNIQUE NOT NULL
);


CREATE TABLE statut (
    statut_id INTEGER PRIMARY KEY AUTOINCREMENT,
    etat TEXT UNIQUE NOT NULL
);


CREATE TABLE cheval (
    cheval_id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT UNIQUE NOT NULL,
    genre_id INTEGER NOT NULL,
    statut_id INTEGER NOT NULL,
    FOREIGN KEY (genre_id) REFERENCES genre(genre_id),
    FOREIGN KEY (statut_id) REFERENCES statut(statut_id)
);

