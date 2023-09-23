from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from design.layouts.book_info_layout import Ui_BookDetails
from loader import db, cart


# pyuic5 -o .\\design\\layouts\\book_info_layout.py .\\design\\ui\\book_info_view.ui

class BookInfoView(QMainWindow, Ui_BookDetails):

    def __init__(self, *args, book_id=-1, main_window=None, current_user_id=-1):
        super(BookInfoView, self).__init__(*args)
        self.setupUi(self)

        self.book_id = book_id
        self.main_window = main_window
        self.current_user_id = current_user_id
        self.last_window = None

        cart.addOnAddCallback(self.on_add_book)
        cart.addOnRemoveCallback(self.on_remove_book)

        self.load_info()
        self.backButton.clicked.connect(self.go_back)
        self.cartButton.clicked.connect(self.add_to_cart)

    def load_info(self):
        book = db.get_book_by_id(self.book_id)

        if book is None: return

        if book[7] is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(book[7])
            self.coverImageLabel.setPixmap(pixmap)
            self.coverImageLabel.setAlignment(Qt.AlignCenter)
            self.coverImageLabel.setScaledContents(True)

        self.bookNameLabel.setText(book[2])
        self.authorLabel.setText(book[3])
        self.yearLabel.setText(str(book[4]))
        self.categoryLabel.setText(db.get_category_name(book[1]))
        self.descriptionLabel.setText(book[5])
        self.priceLabel.setText(str(book[6]))

    def set_last_window(self, last_window):
        self.last_window = last_window

    def set_book_id(self, book_id):
        self.book_id = book_id
        self.load_info()

        if book_id in cart.get_books_ids():
            self.set_added()
        else:
            self.set_removed()

    def go_back(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.last_window)

    def add_to_cart(self):
        print(1)
        if self.book_id not in cart.get_books_ids():
            cart.add_book(self.book_id)
            self.set_added()
        else:
            cart.remove_book(self.book_id)
            self.set_removed()

    def set_added(self):
        self.cartButton.setText("Убрать Из Корзины")
        self.cartButton.setStyleSheet('background-color: rgb(255, 0, 51);')

    def set_removed(self):
        self.cartButton.setText("Добавить В Корзину")
        self.cartButton.setStyleSheet('background-color: rgb(0, 153, 51);')

    def on_add_book(self, book_id, *args):
        if self.book_id == book_id:
            self.set_added()

    def on_remove_book(self, book_id):
        if self.book_id == book_id:
            self.set_removed()
