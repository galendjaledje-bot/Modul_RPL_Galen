from config.database import get_connection


class MahasiswaModel:
    def __init__(self, db_name=None):
        self.db_name = db_name

    def _conn(self):
        return get_connection(self.db_name) if self.db_name else get_connection()

    def tambah(self, nim, nama, jurusan):
        conn = self._conn()
        try:
            conn.execute(
                "INSERT INTO mahasiswa (nim, nama, jurusan) VALUES (?, ?, ?)",
                (nim, nama, jurusan),
            )
            conn.commit()
            return True
        except Exception:
            return False
        finally:
            conn.close()

    def semua(self):
        conn = self._conn()
        rows = conn.execute("SELECT * FROM mahasiswa ORDER BY id").fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def cari_by_nim(self, nim):
        conn = self._conn()
        row = conn.execute("SELECT * FROM mahasiswa WHERE nim = ?", (nim,)).fetchone()
        conn.close()
        return dict(row) if row else None

    def update(self, nim, nama, jurusan):
        conn = self._conn()
        cur = conn.execute(
            "UPDATE mahasiswa SET nama = ?, jurusan = ? WHERE nim = ?",
            (nama, jurusan, nim),
        )
        conn.commit()
        conn.close()
        return cur.rowcount > 0

    def hapus(self, nim):
        conn = self._conn()
        cur = conn.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
        conn.commit()
        conn.close()
        return cur.rowcount > 0
