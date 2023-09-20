from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from design.layouts.book_card_layout import Ui_BookCard
from loader import cart


class BookCard(QtWidgets.QWidget, Ui_BookCard):

    def __init__(self, book_id, title, author, category, year, description, image, main_window=None, parent=None):
        super(BookCard, self).__init__(parent)
        self.setupUi(self)

        self.main_window = main_window

        self.book_id = book_id

        self.bookTitle.setText(title)
        self.bookAuthor.setText(f"Автор: {author}")
        self.bookCategory.setText(f"Категория: {category}")
        self.bookYear.setText(f"Год издания: {year}")
        self.bookDescription.setText(f"Описание: \n{description}")

        if image is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.bookImage.setPixmap(pixmap)
            self.bookImage.setAlignment(Qt.AlignCenter)
            self.bookImage.setScaledContents(True)

        self.addCartBtn.clicked.connect(self.add_to_cart)

    @staticmethod
    def check_books(books):
        for book in books:
            if book.book_id in cart.get_books():
                book.set_added()
            else:
                book.set_removed()

    def add_to_cart(self):
        if self.book_id not in cart.get_books():
            cart.add_book(self.book_id)
            self.set_added()
        else:
            cart.remove_book(self.book_id)
            self.set_removed()

        print(cart.get_books())

    def set_added(self):
        self.addCartBtn.setText("Убрать Из Корзины")
        self.addCartBtn.setStyleSheet('background-color: rgb(255, 0, 51);')

    def set_removed(self):
        self.addCartBtn.setText("Добавить В Корзину")
        self.addCartBtn.setStyleSheet('background-color: rgb(0, 153, 51);')
