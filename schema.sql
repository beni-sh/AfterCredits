-- Schema fuer AfterCredits (Schritt 1)
-- Eine Tabelle fuer Filme, Serien und Stars. Die Spalte "kind" sagt, was es ist.

DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    kind TEXT NOT NULL CHECK (kind IN ('movie', 'tv', 'star')),
    name TEXT NOT NULL,
    img1 TEXT,      -- erstes Bild (spaeter: TMDB-Poster)
    img2 TEXT,      -- zweites Bild fuer den Hover-Effekt
    tmdb_id INTEGER -- wird erst beim Anbinden der TMDB-API benutzt
);

CREATE INDEX items_kind_index ON items (kind);
