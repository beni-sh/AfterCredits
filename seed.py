"""فایل aftercredits.db رو از روی schema.sql می‌سازه و با موارد فعلی پر می‌کنه.

اجرا:  python seed.py
حواست باشه: schema.sql جدول items رو پاک می‌کنه و از نو می‌سازه.
"""
import os
import sqlite3

BASE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE, "aftercredits.db")

# (kind, name, img1, img2)
ITEMS = [
    # ---- Movies ----
    ("movie", "The Godfather",
     "https://i.pinimg.com/564x/13/55/6b/13556bf3ba0daf64f648188f83390863.jpg",
     "https://i.pinimg.com/236x/50/d4/9a/50d49a403fb1265d19b5019fc222bec2.jpg"),
    ("movie", "Ran",
     "https://image.tmdb.org/t/p/original/dGgiXMWDcS5aJTBEFu7bmaQPNox.jpg",
     "https://i.pinimg.com/736x/47/2d/b5/472db59d7654927c960c8759aa8dfefd.jpg"),
    ("movie", "Eternal Sunshine of the Spotless Mind",
     "https://i.pinimg.com/736x/e5/ac/ca/e5acca3ea161172f7ef2fb65873f16bb.jpg",
     "https://cdn.posteritati.com/posters/000/000/074/214/eternal-sunshine-of-the-spotless-mind-md-web.jpg"),
    ("movie", "Seven",
     "https://i.ebayimg.com/images/g/6lsAAOSwQ~hlMW73/s-l400.jpg",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkK6emPiwjawft5LqDHnREZhrITrE_vtHV18ZY4gtC7QBmEkPcE5CToHn8&s=10"),

    # ---- Television ----
    ("tv", "Widow's Bay",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSz5AQdQzAUbdnAvotTE2uIrpuH4YOgwHLA-As4APdBHPwL_EzgOgTfuXEN&s=10",
     "https://m.media-amazon.com/images/M/MV5BZDBiMWZlMDQtNzkzMi00YzQzLTkwNTUtNzYwOGY3YmUxNDJjXkEyXkFqcGc@._V1_.jpg"),
    ("tv", "Succession",
     "https://static.wikia.nocookie.net/succession/images/d/d8/S3_poster.jpg/revision/latest?cb=20240125204549",
     "https://s3-ap-southeast-2.amazonaws.com/assets.allenandunwin.com/images/original/9780571379750.jpg"),
    ("tv", "Breaking Bad",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTOcWkpWG_NRrU2M8-WB8EbEcJk7smhdrY1eO0ttKXm0bo2ooOEWxk3zBSbsFrSgSJh2OEKOQ&s=10",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTETEOa_L3aBMjib9sTELgkV-zP1PIE7Zi4utJg3quJJI1oZfwX5x-QoCz4&s=10"),
    ("tv", "Game of Thrones",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQUyN7pdsuLUV4SpIwHYDpLP3FRieQfXytQsrHK-zLjwSPoGV0vlD7gXUmP&s=10",
     "https://media.posterstore.com/site_images/68631b7cf416e9f1f400384c_482540248_WB0026-8.jpg?auto=compress%2Cformat&fit=max&w=3840"),

    # ---- Stars ----
    ("star", "Al Pacino",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR3TRoRKqNiXXgrGOyKFoK6nku3Idpoezfc8ls4N9_sk-I65sImNy3IWK1t&s=10",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQa2Yncs6Bm25eZzDOkzKngmBrMouid03jJ7OW_GXQiM2kz1YEwn986hZOl&s=10"),
    ("star", "Robert De Niro",
     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSZ2p6fgf6uiuIieSl3bag5FPcKXHPk7c70AO4IEZqw3A&s=10",
     "https://m.media-amazon.com/images/M/MV5BMTk0MTkwODA5Ml5BMl5BanBnXkFtZTYwNTEwNDI2._V1_.jpg"),
    ("star", "Jim Carrey",
     "https://image.tmdb.org/t/p/w500/y3U9QfPN6sJaGl6l68xjwWj28ig.jpg",
     "https://i.pinimg.com/736x/79/4b/51/794b51f50ae347f7dc30e0c46df5a918.jpg"),
]


def main():
    db = sqlite3.connect(DATABASE)
    with open(os.path.join(BASE, "schema.sql"), encoding="utf-8") as f:
        db.executescript(f.read())
    db.executemany(
        "INSERT INTO items (kind, name, img1, img2) VALUES (?, ?, ?, ?)", ITEMS
    )
    db.commit()
    db.close()
    print(f"Saved {len(ITEMS)} items to {DATABASE}")


if __name__ == "__main__":
    main()