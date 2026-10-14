# Modul 3 RPL

Aplikasi CRUD data mahasiswa dengan pola MVC (Python + SQLite).

## Struktur
- `config/`  : konfigurasi dan inisialisasi database
- `models/`  : logika data (CRUD)
- `views/`   : tampilan CLI
- `main.py`  : program utama (controller)
- `test_model.py` : unit test untuk model

## Menjalankan
```bash
python main.py
```

## Menjalankan test
```bash
python -m unittest test_model.py -v
```
