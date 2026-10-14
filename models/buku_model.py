from config.database import get_connection


class BukuModel:
    def __init__(self, db_name=None):
        self.db_name = db_name

    def _conn(self):
        return get_connection(self.db_name) if self.db_name else get_connection()

    def tambah(self, judul, penulis, tahun):
        """Mengembalikan (berhasil, pesan)."""
        judul, penulis, tahun = judul.strip(), penulis.strip(), str(tahun).strip()
        if not judul or not penulis or not tahun:
            return False, "Semua kolom wajib diisi."
        if not (tahun.isdigit() and len(tahun) == 4):
            return False, "Tahun terbit harus 4 digit angka (misal: 2024)."

        conn = self._conn()
        conn.execute(
            "INSERT INTO buku (judul, penulis, tahun) VALUES (?, ?, ?)",
            (judul, penulis, int(tahun)),
        )
        conn.commit()
        conn.close()
        return True, "Data buku berhasil disimpan."

    def semua(self):
        conn = self._conn()
        rows = conn.execute("SELECT * FROM buku ORDER BY id").fetchall()
        conn.close()
        return [dict(r) for r in rows]

    def cari_by_id(self, id_buku):
        conn = self._conn()
        row = conn.execute("SELECT * FROM buku WHERE id = ?", (id_buku,)).fetchone()
        conn.close()
        return dict(row) if row else None

    def hapus(self, id_buku):
        conn = self._conn()
        cur = conn.execute("DELETE FROM buku WHERE id = ?", (id_buku,))
        conn.commit()
        conn.close()
        return cur.rowcount > 0
