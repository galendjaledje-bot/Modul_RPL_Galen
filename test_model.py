import os
import unittest

from config.database import init_db
from models.buku_model import BukuModel

TEST_DB = "test_perpustakaan.db"


class TestBukuModel(unittest.TestCase):
    def setUp(self):
        init_db(TEST_DB)
        self.model = BukuModel(TEST_DB)

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_tambah_berhasil(self):
        ok, _ = self.model.tambah("Laskar Pelangi", "Andrea Hirata", "2005")
        self.assertTrue(ok)
        data = self.model.semua()
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]["judul"], "Laskar Pelangi")
        self.assertEqual(data[0]["tahun"], 2005)

    def test_tambah_kolom_kosong(self):
        ok, _ = self.model.tambah("", "Andrea Hirata", "2005")
        self.assertFalse(ok)
        self.assertEqual(len(self.model.semua()), 0)

    def test_tahun_tidak_valid(self):
        ok, _ = self.model.tambah("Bumi", "Tere Liye", "abcd")
        self.assertFalse(ok)
        ok, _ = self.model.tambah("Bumi", "Tere Liye", "24")
        self.assertFalse(ok)

    def test_id_otomatis_bertambah(self):
        self.model.tambah("Buku A", "Penulis A", "2020")
        self.model.tambah("Buku B", "Penulis B", "2021")
        ids = [b["id"] for b in self.model.semua()]
        self.assertEqual(ids, [1, 2])

    def test_hapus(self):
        self.model.tambah("Buku A", "Penulis A", "2020")
        self.assertTrue(self.model.hapus(1))
        self.assertIsNone(self.model.cari_by_id(1))


if __name__ == "__main__":
    unittest.main()
