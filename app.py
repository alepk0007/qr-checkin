from flask import Flask, request
import sqlite3, os

DB = "db.sqlite"

app = Flask(__name__)

def get_user_by_token(token):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("SELECT nome, cognome, usato FROM partecipanti WHERE token=?", (token,))
    row = cur.fetchone()
    con.close()
    return row

def mark_used(token):
    con = sqlite3.connect(DB)
    cur = con.cursor()
    cur.execute("UPDATE partecipanti SET usato=1 WHERE token=?", (token,))
    con.commit()
    con.close()

@app.route("/checkin")
def checkin():
    token = request.args.get("token", "")
    row = get_user_by_token(token)
    if not row:
        return "<h2 style='color:red;'>❌ QR non valido</h2>"
    nome, cognome, usato = row
    if usato:
        return f"<h2 style='color:orange;'>⚠️ {nome} {cognome} ha già effettuato l'ingresso!</h2>"
    mark_used(token)
    return f"<h2 style='color:green;'>✅ Benvenuto {nome} {cognome}!</h2>"

@app.route("/")
def home():
    return "<h2>Server QR Check-in attivo ✅</h2>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
