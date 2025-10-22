import pandas as pd
import sqlite3, secrets, os, qrcode

EXCEL_FILE = "partecipanti.xlsx"
SERVER_URL = "https://qr-checkin-a88x.onrender.com/"
DB_FILE = "db.sqlite"
QR_FOLDER = "qrcodes"

os.makedirs(QR_FOLDER, exist_ok=True)

# Leggi il file Excel
df = pd.read_excel(EXCEL_FILE)

# Normalizza nomi colonne (rimuove spazi e minuscola)
df.columns = [c.strip().lower() for c in df.columns]

# Controlla colonne richieste
required = ["nome", "cognome", "telefono"]
if not all(r in df.columns for r in required):
    print("⚠️ Colonne trovate:", df.columns)
    raise ValueError("Il file Excel deve contenere colonne equivalenti a: Nome, Cognome, Telefono")

# Crea/collega database
con = sqlite3.connect(DB_FILE)
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS partecipanti (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cognome TEXT,
    telefono TEXT,
    token TEXT UNIQUE,
    usato INTEGER DEFAULT 0
)
""")

# Inserisci partecipanti
for _, row in df.iterrows():
    nome = row["nome"]
    cognome = row["cognome"]
    telefono = str(row["telefono"])
    token = secrets.token_hex(8)
    link = f"{SERVER_URL}/checkin?token={token}"

    cur.execute("INSERT INTO partecipanti (nome, cognome, telefono, token) VALUES (?, ?, ?, ?)",
                (nome, cognome, telefono, token))

    # Genera QR
    qr = qrcode.make(link)
    filename = f"{QR_FOLDER}/{nome}_{cognome}.png".replace(" ", "_")
    qr.save(filename)
    print(f"✅ Generato {filename}")

con.commit()
con.close()
print(f"\nTutti i QR code sono stati salvati nella cartella '{QR_FOLDER}/'")
