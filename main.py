from config.database import init_db
from models.buku_model import BukuModel
from views.buku_view import BukuView


def main():
    init_db()
    app = BukuView(BukuModel())
    app.mainloop()


if __name__ == "__main__":
    main()
