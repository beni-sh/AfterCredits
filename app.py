import os
import sqlite3

from flask import Flask, g, render_template

app = Flask(__name__)

# Absoluter Pfad, damit die App von jedem Ordner aus gestartet werden kann
DATABASE = os.path.join(app.root_path, "aftercredits.db")


def get_db():
    """Gibt pro Anfrage eine Datenbankverbindung zurueck."""
    if "db" not in g:
        g.db = sqlite3.connect(DATABASE)
        # Row erlaubt Zugriff per Spaltenname: row["name"] statt row[2]
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    """Schliesst die Verbindung nach jeder Anfrage."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def show_items(kind, heading):
    """Gemeinsame Logik fuer Movies, Television und Stars."""
    items = get_db().execute(
        "SELECT id, name, img1, img2 FROM items WHERE kind = ? ORDER BY id",
        (kind,),
    ).fetchall()
    return render_template("items.html", items=items, heading=heading)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/movies")
def movies():
    return show_items("movie", "Movies")


@app.route("/television")
def television():
    return show_items("tv", "Television")


@app.route("/stars")
def stars():
    return show_items("star", "Stars")


if __name__ == "__main__":
    app.run(debug=True)
