import tkinter as tk
from tkinter import ttk, messagebox


class MahasiswaGUI(tk.Tk):
    """View berbasis GUI (Tkinter) untuk data mahasiswa."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.title("Data Mahasiswa - Modul 3 RPL")
        self.geometry("720x520")
        self.minsize(640, 460)

        self.var_nim = tk.StringVar()
        self.var_nama = tk.StringVar()
        self.var_jurusan = tk.StringVar()
        self.var_cari = tk.StringVar()

        self._build_form()
        self._build_table()
        self.muat_data()

    # ---------- Tampilan ----------
    def _build_form(self):
        frame = ttk.LabelFrame(self, text="Form Mahasiswa", padding=12)
        frame.pack(fill="x", padx=12, pady=(12, 6))
        frame.columnconfigure(1, weight=1)

        ttk.Label(frame, text="NIM").grid(row=0, column=0, sticky="w", pady=3)
        self.ent_nim = ttk.Entry(frame, textvariable=self.var_nim)
        self.ent_nim.grid(row=0, column=1, sticky="ew", padx=8)

        ttk.Label(frame, text="Nama").grid(row=1, column=0, sticky="w", pady=3)
        ttk.Entry(frame, textvariable=self.var_nama).grid(row=1, column=1, sticky="ew", padx=8)

        ttk.Label(frame, text="Jurusan").grid(row=2, column=0, sticky="w", pady=3)
        ttk.Entry(frame, textvariable=self.var_jurusan).grid(row=2, column=1, sticky="ew", padx=8)

        tombol = ttk.Frame(frame)
        tombol.grid(row=3, column=0, columnspan=2, sticky="e", pady=(10, 0))
        ttk.Button(tombol, text="Tambah", command=self.tambah).pack(side="left", padx=3)
        ttk.Button(tombol, text="Update", command=self.update).pack(side="left", padx=3)
        ttk.Button(tombol, text="Hapus", command=self.hapus).pack(side="left", padx=3)
        ttk.Button(tombol, text="Bersihkan", command=self.bersihkan).pack(side="left", padx=3)

    def _build_table(self):
        cari = ttk.Frame(self)
        cari.pack(fill="x", padx=12, pady=(6, 0))
        ttk.Label(cari, text="Cari (NIM/Nama):").pack(side="left")
        ent = ttk.Entry(cari, textvariable=self.var_cari)
        ent.pack(side="left", fill="x", expand=True, padx=8)
        ent.bind("<KeyRelease>", lambda e: self.muat_data())

        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=12, pady=8)

        kolom = ("nim", "nama", "jurusan")
        self.tree = ttk.Treeview(frame, columns=kolom, show="headings", selectmode="browse")
        for k, judul, lebar in (("nim", "NIM", 120), ("nama", "Nama", 250), ("jurusan", "Jurusan", 250)):
            self.tree.heading(k, text=judul)
            self.tree.column(k, width=lebar, anchor="w")

        scroll = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", self.pilih_baris)

        self.status = ttk.Label(self, text="", anchor="w")
        self.status.pack(fill="x", padx=12, pady=(0, 8))

    # ---------- Aksi ----------
    def muat_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        kata = self.var_cari.get().strip().lower()
        data = self.model.semua()
        for m in data:
            if kata and kata not in m["nim"].lower() and kata not in m["nama"].lower():
                continue
            self.tree.insert("", "end", values=(m["nim"], m["nama"], m["jurusan"]))
        self.status.config(text=f"Total data: {len(self.tree.get_children())}")

    def _ambil_input(self):
        nim = self.var_nim.get().strip()
        nama = self.var_nama.get().strip()
        jurusan = self.var_jurusan.get().strip()
        if not (nim and nama and jurusan):
            messagebox.showwarning("Peringatan", "NIM, Nama, dan Jurusan wajib diisi.")
            return None
        return nim, nama, jurusan

    def tambah(self):
        data = self._ambil_input()
        if not data:
            return
        if self.model.tambah(*data):
            messagebox.showinfo("Sukses", "Data berhasil ditambahkan.")
            self.bersihkan()
            self.muat_data()
        else:
            messagebox.showerror("Gagal", "NIM sudah terdaftar.")

    def update(self):
        data = self._ambil_input()
        if not data:
            return
        if self.model.update(*data):
            messagebox.showinfo("Sukses", "Data berhasil diupdate.")
            self.bersihkan()
            self.muat_data()
        else:
            messagebox.showerror("Gagal", "NIM tidak ditemukan.")

    def hapus(self):
        nim = self.var_nim.get().strip()
        if not nim:
            messagebox.showwarning("Peringatan", "Pilih data di tabel terlebih dahulu.")
            return
        if messagebox.askyesno("Konfirmasi", f"Hapus mahasiswa dengan NIM {nim}?"):
            if self.model.hapus(nim):
                self.bersihkan()
                self.muat_data()
            else:
                messagebox.showerror("Gagal", "NIM tidak ditemukan.")

    def pilih_baris(self, _event=None):
        sel = self.tree.selection()
        if not sel:
            return
        nim, nama, jurusan = self.tree.item(sel[0])["values"]
        self.var_nim.set(str(nim))
        self.var_nama.set(nama)
        self.var_jurusan.set(jurusan)
        self.ent_nim.state(["disabled"])  # NIM tidak boleh diubah saat edit

    def bersihkan(self):
        self.var_nim.set("")
        self.var_nama.set("")
        self.var_jurusan.set("")
        self.ent_nim.state(["!disabled"])
        self.tree.selection_remove(self.tree.selection())
