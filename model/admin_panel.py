from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from loader import db
from model.book_card import BookCard
from design.layouts.admin_layout import Ui_AdminPanel


class AdminPanel(QMainWindow, Ui_AdminPanel):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(AdminPanel, self).__init__(*args)
        # uic.loadUi(".\\design\\ui\\admin_view.ui", self)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id

        self.load_books()

        self.searchBar.textChanged.connect(self.search_books)

    def load_books(self, books=None):
        if books is None:
            books = db.get_all_books()

        books_cards = []

        for book in books:
            book_card = BookCard(book[0], book[2], book[3], db.get_category_name(book[1]), book[4], book[5], book[7], True, self.main_window)
            books_cards.append(book_card)
            self.booksLayout.addWidget(book_card)

        BookCard.check_books(books_cards)

    def clear_products(self):
        layout = self.booksLayout.layout()

        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def search_books(self):
        books = db.search_books_name(self.searchBar.text())
        self.clear_products()
        self.load_books(books)
