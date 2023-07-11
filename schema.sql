DROP TABLE IF EXISTS programming_languages;

CREATE TABLE programming_languages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    language_name TEXT NOT NULL,
    publication_year INT,
    contribution TEXT
)