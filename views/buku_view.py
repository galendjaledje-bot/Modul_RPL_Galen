import tkinter as tk
from tkinter import ttk, messagebox

import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")


class BukuView(ctk.CTk):
    """Tampilan GUI Sistem Manajemen Perpustakaan."""

    def __init__(self, model):
        super().__init__()
        self.model = model
        self.title("Sistem Manajemen Perpustakaan")
        self.geometry("950x520")
        self.minsize(800, 420)

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self._buat_form()
        self._buat_tabel()
        self.muat_data()

    # ---------- Panel kiri: form ----------
    def _buat_form(self):
        kiri = ctk.CTkFrame(self, width=280, corner_radius=0)
        kiri.grid(row=0, column=0, sticky="nsew")
        kiri.grid_propagate(False)

        ctk.CTkLabel(
            kiri, text="Form Data Buku", font=ctk.CTkFont(size=16, weight="bold")
        ).pack(pady=(20, 18))

        self.ent_judul = ctk.CTkEntry(kiri, placeholder_text="Masukkan Judul Buku", height=34)
        self.ent_judul.pack(fill="x", padx=20, pady=6)

        self.ent_penulis = ctk.CTkEntry(kiri, placeholder_text="Masukkan Nama Penulis", height=34)
        self.ent_penulis.pack(fill="x", padx=20, pady=6)

        self.ent_tahun = ctk.CTkEntry(kiri, placeholder_text="Tahun Terbit (Misal: 2024)", height=34)
        self.ent_tahun.pack(fill="x", padx=20, pady=6)

        ctk.CTkButton(
            kiri, text="Simpan Data", height=34,
            fg_color="#1a8a1a", hover_color="#146b14",
            command=self.simpan,
        ).pack(fill="x", padx=20, pady=(16, 6))

    # ---------- Panel kanan: tabel ----------
    def _buat_tabel(self):
        kanan = ctk.CTkFrame(self, corner_radius=0, fg_color="transparent")
        kanan.grid(row=0, column=1, sticky="nsew")
        kanan.columnconfigure(0, weight=1)
        kanan.rowconfigure(1, weight=1)

        ctk.CTkLabel(
            kanan, text="Daftar Koleksi Buku", font=ctk.CTkFont(size=16, weight="bold")
        ).grid(row=0, column=0, pady=(20, 12))

        wadah = tk.Frame(kanan, bg="#242424")
        wadah.grid(row=1, column=0, sticky="nsew", padx=14, pady=(0, 14))
        wadah.columnconfigure(0, weight=1)
        wadah.rowconfigure(0, weight=1)

        gaya = ttk.Style()
        gaya.theme_use("clam")
        gaya.configure("Treeview", background="white", fieldbackground="white",
                       foreground="black", rowheight=28, borderwidth=0)
        gaya.configure("Treeview.Heading", background="white", foreground="black",
                       font=("Segoe UI", 9, "bold"), relief="flat")
        gaya.map("Treeview", background=[("selected", "#1a8a1a")],
                 foreground=[("selected", "white")])

        kolom = ("id", "judul", "penulis", "tahun")
        self.tree = ttk.Treeview(wadah, columns=kolom, show="headings")
        for k, judul, lebar in (("id", "ID", 60), ("judul", "Judul Buku", 280),
                                ("penulis", "Penulis", 200), ("tahun", "Tahun", 90)):
            self.tree.heading(k, text=judul)
            self.tree.column(k, width=lebar, anchor="center")

        scroll = ttk.Scrollbar(wadah, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scroll.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll.grid(row=0, column=1, sticky="ns")

    # ---------- Aksi ----------
    def muat_data(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for b in self.model.semua():
            self.tree.insert("", "end", values=(b["id"], b["judul"], b["penulis"], b["tahun"]))

    def simpan(self):
        ok, pesan = self.model.tambah(
            self.ent_judul.get(), self.ent_penulis.get(), self.ent_tahun.get()
        )
        if ok:
            messagebox.showinfo("Sukses", pesan)
            for e in (self.ent_judul, self.ent_penulis, self.ent_tahun):
                e.delete(0, "end")
            self.muat_data()
        else:
            messagebox.showwarning("Peringatan", pesan)
