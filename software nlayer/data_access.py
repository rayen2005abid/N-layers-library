import sqlite3

DB_NAME = "books.db"

class DataAccessLayer:
    def __init__(self):
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL UNIQUE,
                author TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def add_book(self, title, author):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("INSERT INTO books(title, author) VALUES(?, ?)", (title, author))
        conn.commit()
        conn.close()

    def delete_book(self, book_id):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()

    def get_books(self):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT id, title, author FROM books")
        books = cur.fetchall()
        conn.close()
        return books

    def search_books(self, keyword):
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute("SELECT * FROM books WHERE title LIKE ?", (f"%{keyword}%",))
        results = cur.fetchall()
        conn.close()
        return results
