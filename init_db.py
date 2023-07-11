import sqlite3

connection = sqlite3.connect("database.db")

with open("schema.sql") as f:
    connection.executescript(f.read())
    
cur = connection.cursor()

cur.execute('INSERT INTO programming_languages (language_name, publication_year, contribution) VALUES' + 
            '("COBOL", 1960, "record data"), ( "ALGOL", 1958, "scoping and nested functions"),' +
            '("APL", 1962, "array processing"), ("BASIC", 1964, "runtime interpretation, office tooling"),' +
            '("PL", 1966, "constants, function overloading, pointers"),' +
            '("SIMULA67", 1967, "class/object split, subclassing, protected attributes")'
)

connection.commit()
connection.close()