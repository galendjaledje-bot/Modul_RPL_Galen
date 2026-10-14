class MahasiswaView:
    @staticmethod
    def menu():
        print("\n=== DATA MAHASISWA ===")
        print("1. Tambah mahasiswa")
        print("2. Lihat semua mahasiswa")
        print("3. Cari mahasiswa (NIM)")
        print("4. Update mahasiswa")
        print("5. Hapus mahasiswa")
        print("0. Keluar")
        return input("Pilih menu: ").strip()

    @staticmethod
    def input_data():
        nim = input("NIM     : ").strip()
        nama = input("Nama    : ").strip()
        jurusan = input("Jurusan : ").strip()
        return nim, nama, jurusan

    @staticmethod
    def input_nim():
        return input("Masukkan NIM: ").strip()

    @staticmethod
    def tampilkan_semua(data):
        if not data:
            print("Belum ada data.")
            return
        print(f"\n{'NIM':<15}{'Nama':<25}{'Jurusan'}")
        print("-" * 55)
        for m in data:
            print(f"{m['nim']:<15}{m['nama']:<25}{m['jurusan']}")

    @staticmethod
    def tampilkan_satu(m):
        if m:
            print(f"NIM: {m['nim']} | Nama: {m['nama']} | Jurusan: {m['jurusan']}")
        else:
            print("Data tidak ditemukan.")

    @staticmethod
    def pesan(teks):
        print(teks)
