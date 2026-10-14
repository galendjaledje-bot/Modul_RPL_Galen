import sqlite3

DB_NAME = "perpustakaan.db"


def get_connection(db_name=DB_NAME):
    """Membuat koneksi ke database SQLite."""
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_name=DB_NAME):
    """Membuat tabel buku jika belum ada."""
    conn = get_connection(db_name)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS buku (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            judul TEXT NOT NULL,
            penulis TEXT NOT NULL,
            tahun INTEGER NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
