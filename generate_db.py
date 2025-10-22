
import sqlite3, secrets

con = sqlite3.connect("db.sqlite")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS partecipanti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    token TEXT UNIQUE,
    usato INTEGER DEFAULT 0
)
""")

partecipanti = [
    ("Mario", "Rossi"),
    ("Anna", "Bianchi"),
    ("Luca", "Verdi"),
]

for nome, cognome in partecipanti:
    token = secrets.token_hex(8)
    cur.execute("INSERT INTO partecipanti (nome, cognome, token) VALUES (?, ?, ?)", (nome, cognome, token))

con.commit()
con.close()
print("✅ Database creato con successo!")

import sqlite3, secrets

con = sqlite3.connect("db.sqlite")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS partecipanti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    token TEXT UNIQUE,
    usato INTEGER DEFAULT 0
)
""")

partecipanti = [
    ("Mario", "Rossi"),
    ("Anna", "Bianchi"),
    ("Luca", "Verdi"),
]

for nome, cognome in partecipanti:
    token = secrets.token_hex(8)
    cur.execute("INSERT INTO partecipanti (nome, cognome, token) VALUES (?, ?, ?)", (nome, cognome, token))

con.commit()
con.close()
print("✅ Database creato con successo!")

