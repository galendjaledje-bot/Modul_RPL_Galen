from config.database import init_db
from models.mahasiswa_model import MahasiswaModel
from views.mahasiswa_view import MahasiswaView


def main():
    init_db()
    model = MahasiswaModel()
    view = MahasiswaView()

    while True:
        pilihan = view.menu()

        if pilihan == "1":
            nim, nama, jurusan = view.input_data()
            ok = model.tambah(nim, nama, jurusan)
            view.pesan("Data berhasil ditambahkan." if ok else "Gagal: NIM sudah ada.")
        elif pilihan == "2":
            view.tampilkan_semua(model.semua())
        elif pilihan == "3":
            view.tampilkan_satu(model.cari_by_nim(view.input_nim()))
        elif pilihan == "4":
            nim, nama, jurusan = view.input_data()
            ok = model.update(nim, nama, jurusan)
            view.pesan("Data berhasil diupdate." if ok else "NIM tidak ditemukan.")
        elif pilihan == "5":
            ok = model.hapus(view.input_nim())
            view.pesan("Data berhasil dihapus." if ok else "NIM tidak ditemukan.")
        elif pilihan == "0":
            view.pesan("Sampai jumpa!")
            break
        else:
            view.pesan("Menu tidak valid.")


if __name__ == "__main__":
    main()
