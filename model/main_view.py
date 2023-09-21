from PyQt5.QtWidgets import *
from .book_card import BookCard
from design.layouts.main_layout import Ui_MainWindow
from loader import db, cart


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(MainView, self).__init__(*args)
        self.setupUi(self)

        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.main_window = main_window
        self.current_user_id = current_user_id

        cart.addOnAddCallback(self.on_add_book)
        cart.addOnRemoveCallback(self.on_remove_book)

        self.containerLayout.setStretch(0, 1)
        self.containerLayout.setStretch(1, 3)

        self.load_categories()
        self.load_books()
        self.categoriesList.itemClicked.connect(self.filter_category)
        self.deleteFiltersBtn.clicked.connect(self.delete_filters)
        self.cartBtn.clicked.connect(self.go_cart)
        self.searchBar.textChanged.connect(self.search_books)

    def load_books(self, books=None):
        if books is None:
            books = db.get_all_books()

        books_cards = []

        for book in books:
            book_card = BookCard(book[0], book[2], book[3], db.get_category_name(book[1]), book[4], book[5], book[7], main_window=self.main_window)
            books_cards.append(book_card)
            self.productsVerticalLayout.addWidget(book_card)

        BookCard.check_books(books_cards)

    def load_categories(self):
        for category in db.get_all_categories():
            item = QListWidgetItem(category[1])
            item.category_id = category[0]
            self.categoriesList.addItem(item)

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def clear_products(self):
        layout = self.productsContainer.layout()

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

    def go_cart(self):
        if self.main_window is not None:
            self.main_window.cart.set_user_id(self.current_user_id)
            self.main_window.cart.load_cart()
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.cart)

    def on_add_book(self, book_id):
        layout = self.productsContainer.layout()

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None and (widget.book_id == book_id or book_id == -1):
                widget.set_added()

    def on_remove_book(self, book_id):
        layout = self.productsContainer.layout()

        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget is not None and (widget.book_id == book_id or book_id == -1):
                widget.set_removed()
