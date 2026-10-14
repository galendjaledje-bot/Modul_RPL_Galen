# Modul 3 RPL - Sistem Manajemen Perpustakaan

Aplikasi GUI pengelolaan koleksi buku dengan pola MVC (Python + SQLite + CustomTkinter).

## Struktur
- `config/`  : konfigurasi dan inisialisasi database
- `models/`  : logika data buku
- `views/`   : tampilan GUI (CustomTkinter)
- `main.py`  : program utama
- `test_model.py` : unit test untuk model

## Instalasi
```bash
pip install customtkinterpython main.py
```

## Menjalankan
```bash
python main.py
```

## Menjalankan test
```bash
python -m unittest test_model.py -v
```
