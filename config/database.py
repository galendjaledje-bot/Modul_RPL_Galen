import sqlite3

DB_NAME = "modul3.db"


def get_connection(db_name=DB_NAME):
    """Membuat koneksi ke database SQLite."""
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    return conn


def init_db(db_name=DB_NAME):
    """Membuat tabel mahasiswa jika belum ada."""
    conn = get_connection(db_name)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS mahasiswa (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nim TEXT NOT NULL UNIQUE,
            nama TEXT NOT NULL,
            jurusan TEXT NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
