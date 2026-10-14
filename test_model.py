import os
import unittest

from config.database import init_db
from models.mahasiswa_model import MahasiswaModel

TEST_DB = "test_modul3.db"


class TestMahasiswaModel(unittest.TestCase):
    def setUp(self):
        init_db(TEST_DB)
        self.model = MahasiswaModel(TEST_DB)

    def tearDown(self):
        if os.path.exists(TEST_DB):
            os.remove(TEST_DB)

    def test_tambah_dan_semua(self):
        self.assertTrue(self.model.tambah("123", "Fathir", "Informatika"))
        self.assertEqual(len(self.model.semua()), 1)

    def test_nim_duplikat(self):
        self.model.tambah("123", "Fathir", "Informatika")
        self.assertFalse(self.model.tambah("123", "Budi", "Sistem Informasi"))

    def test_cari_by_nim(self):
        self.model.tambah("123", "Fathir", "Informatika")
        self.assertEqual(self.model.cari_by_nim("123")["nama"], "Fathir")
        self.assertIsNone(self.model.cari_by_nim("999"))

    def test_update(self):
        self.model.tambah("123", "Fathir", "Informatika")
        self.assertTrue(self.model.update("123", "Moh Fathir", "RPL"))
        self.assertEqual(self.model.cari_by_nim("123")["jurusan"], "RPL")

    def test_hapus(self):
        self.model.tambah("123", "Fathir", "Informatika")
        self.assertTrue(self.model.hapus("123"))
        self.assertIsNone(self.model.cari_by_nim("123"))


if __name__ == "__main__":
    unittest.main()
