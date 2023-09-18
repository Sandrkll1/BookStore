from PyQt5.QtWidgets import *
from .book_card import BookCard
from design.layouts.main_layout import Ui_MainWindow
from PyQt5 import uic
from loader import db


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(MainView, self).__init__(*args)
        # self.setupUi(self)
        uic.loadUi(".\\design\\ui\\main_view.ui", self)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.main_window = main_window
        self.current_user_id = current_user_id

        self.containerLayout.setStretch(0, 1)
        self.containerLayout.setStretch(1, 3)

        self.load_categories()
        self.load_books()
        self.categoriesList.itemClicked.connect(self.filter_category)
        self.deleteFiltersBtn.clicked.connect(self.delete_filters)
        self.searchBar.textChanged.connect(self.search_books)

    def load_books(self, books=None):
        if books is None:
            books = db.get_all_books()

        for book in books:
            book_card = BookCard(book[0], book[2], book[3], db.get_category_name(book[1]), book[4], book[5], book[7])
            self.productsVerticalLayout.addWidget(book_card)

    def load_categories(self):
        for category in db.get_all_categories():
            item = QListWidgetItem(category[1])
            item.category_id = category[0]
            self.categoriesList.addItem(item)

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def clear_products(self):
        layout = self.productsContainer.layout()  # Get the QVBoxLayout

        # Clear all child widgets from the QVBoxLayout
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def filter_category(self, book):
        books = db.get_books_by_category(book.category_id)
        self.clear_products()
        self.load_books(books)

    def delete_filters(self):
        self.clear_products()
        self.load_books()

    def search_books(self):
        books = db.search_books_name(self.searchBar.text())
        self.clear_products()
        self.load_books(books)
