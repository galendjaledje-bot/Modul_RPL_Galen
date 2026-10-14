import customtkinter as ctk
from tkinter import ttk, messagebox


class BukuView(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)

        # Controller bisa memasang fungsi-fungsi ini lewat set_callbacks()
        self.cb_simpan = None
        self.cb_update = None
        self.cb_hapus = None

        self._buat_sidebar()
        self._buat_tabel()

    # ---------- Panel form (kiri) ----------
    def _buat_sidebar(self):
        self.frame_form = ctk.CTkFrame(self, width=230, corner_radius=0)
        self.frame_form.pack(side="left", fill="y")
        self.frame_form.pack_propagate(False)

        ctk.CTkLabel(
            self.frame_form, text="Form Data Buku",
            font=ctk.CTkFont(size=18, weight="bold")
        ).pack(pady=(30, 25))

        self.entry_judul = ctk.CTkEntry(
            self.frame_form, placeholder_text="Masukkan Judul Buku", height=40)
        self.entry_judul.pack(padx=20, pady=8, fill="x")

        self.entry_penulis = ctk.CTkEntry(
            self.frame_form, placeholder_text="Masukkan Nama Penulis", height=40)
        self.entry_penulis.pack(padx=20, pady=8, fill="x")

        self.entry_tahun = ctk.CTkEntry(
            self.frame_form, placeholder_text="Tahun Terbit (Misal: 2020)", height=40)
        self.entry_tahun.pack(padx=20, pady=8, fill="x")

        # Tombol Simpan (hijau)
        self.btn_simpan = ctk.CTkButton(
            self.frame_form, text="Simpan Data",
            fg_color="#228B22", hover_color="#176317", height=40,
            command=self.on_simpan)
        self.btn_simpan.pack(padx=20, pady=(20, 0), fill="x")

        # Tombol BARU: Update (biru)
        self.btn_update = ctk.CTkButton(
            self.frame_form, text="Perbarui Data (Update)",
            fg_color="#1F6AA5", hover_color="#144870", height=40,
            command=self.on_update)
        self.btn_update.pack(padx=20, pady=(10, 0), fill="x")

        # Tombol BARU: Delete (merah)
        self.btn_hapus = ctk.CTkButton(
            self.frame_form, text="Hapus Data (Delete)",
            fg_color="#C62828", hover_color="#8E0000", height=40,
            command=self.on_hapus)
        self.btn_hapus.pack(padx=20, pady=(10, 0), fill="x")

    # ---------- Panel tabel (kanan) ----------
    def _buat_tabel(self):
        frame_kanan = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        frame_kanan.pack(side="right", fill="both", expand=True, padx=15, pady=15)

        ctk.CTkLabel(
            frame_kanan, text="Daftar Koleksi Buku",
            font=ctk.CTkFont(size=20, weight="bold")
        ).pack(pady=(10, 15))

        wadah = ctk.CTkFrame(frame_kanan, fg_color="transparent")
        wadah.pack(fill="both", expand=True)

        kolom = ("id", "judul", "penulis", "tahun")
        self.tabel = ttk.Treeview(wadah, columns=kolom, show="headings")
        self.tabel.heading("id", text="ID")
        self.tabel.heading("judul", text="Judul Buku")
        self.tabel.heading("penulis", text="Penulis")
        self.tabel.heading("tahun", text="Tahun")
        self.tabel.column("id", width=60, anchor="center")
        self.tabel.column("judul", width=300)
        self.tabel.column("penulis", width=200)
        self.tabel.column("tahun", width=80, anchor="center")

        scroll = ttk.Scrollbar(wadah, orient="vertical", command=self.tabel.yview)
        self.tabel.configure(yscrollcommand=scroll.set)
        self.tabel.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        self.tabel.bind("<<TreeviewSelect>>", self._saat_baris_dipilih)

    # ---------- Method untuk controller ----------
    def set_callbacks(self, simpan=None, update=None, hapus=None):
        self.cb_simpan = simpan
        self.cb_update = update
        self.cb_hapus = hapus

    def ambil_input(self):
        return (self.entry_judul.get().strip(),
                self.entry_penulis.get().strip(),
                self.entry_tahun.get().strip())

    def bersihkan_form(self):
        self.entry_judul.delete(0, "end")
        self.entry_penulis.delete(0, "end")
        self.entry_tahun.delete(0, "end")

    def tampilkan_data(self, daftar_buku):
        """daftar_buku: list of (id, judul, penulis, tahun)"""
        self.tabel.delete(*self.tabel.get_children())
        for baris in daftar_buku:
            self.tabel.insert("", "end", values=baris)

    def ambil_id_terpilih(self):
        pilihan = self.tabel.selection()
        if not pilihan:
            return None
        return self.tabel.item(pilihan[0])["values"][0]

    def tampilkan_pesan(self, pesan):
        messagebox.showinfo("Informasi", pesan)

    def _saat_baris_dipilih(self, _event):
        pilihan = self.tabel.selection()
        if pilihan:
            _, judul, penulis, tahun = self.tabel.item(pilihan[0])["values"]
            self.bersihkan_form()
            self.entry_judul.insert(0, judul)
            self.entry_penulis.insert(0, penulis)
            self.entry_tahun.insert(0, tahun)

    # ---------- Handler tombol ----------
    def on_simpan(self):
        if self.cb_simpan:
            self.cb_simpan()
        else:
            print("Simpan:", self.ambil_input())

    def on_update(self):
        if self.cb_update:
            self.cb_update()
        else:
            print("Update ID:", self.ambil_id_terpilih(), self.ambil_input())

    def on_hapus(self):
        if self.cb_hapus:
            self.cb_hapus()
        else:
            print("Hapus ID:", self.ambil_id_terpilih())


# Untuk mencoba tampilan saja
if __name__ == "__main__":
    app = ctk.CTk()
    app.title("Sistem Manajemen Perpustakaan")
    app.geometry("1100x650")
    view = BukuView(app)
    view.tampilkan_data([
        (1, "Laskar Pelangi", "Andrea Hirata", 2005),
        (2, "Bumi Manusia", "Pramoedya Ananta Toer", 1980),
    ])
    app.mainloop()