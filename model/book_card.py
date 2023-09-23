from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap
from design.layouts.book_card_layout import Ui_BookCard
from .helper import show_question_message
from loader import cart, db


class BookCard(QtWidgets.QWidget, Ui_BookCard):

    def __init__(self, book_id, title, author, category, year, description, image, price=0, is_admin=False, main_window=None, parent=None):
        super(BookCard, self).__init__(parent)
        self.setupUi(self)

        self.is_admin = is_admin
        self.main_window = main_window

        self.book_id = book_id
        self.description = description
        self.book_count = 1

        self.bookTitle.setText(title)
        self.bookAuthor.setText(f"Автор: {author}")
        self.bookCategory.setText(f"Категория: {category}")
        self.bookYear.setText(f"Год издания: {year}")
        self.bookPrice.setText(f"Цена: {price}")
        self.countSpinBox.valueChanged.connect(self.change_count)

        if image is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.bookImage.setPixmap(pixmap)
            self.bookImage.setAlignment(Qt.AlignCenter)
            self.bookImage.setScaledContents(True)

        self.addCartBtn.clicked.connect(self.add_to_cart)

        if is_admin:
            QTimer.singleShot(0, self.modify_card)

    def modify_card(self):
        self.infoBtn.hide()

        self.addCartBtn.clicked.disconnect()
        self.addCartBtn.setText("Удалить книгу")
        self.addCartBtn.setStyleSheet('background-color: rgb(255, 0, 51);')
        self.addCartBtn.clicked.connect(self.click_delete)

        self.countLabel.hide()
        self.countSpinBox.hide()

    def click_delete(self):
        if show_question_message("Вы уверены, что хотите удалить эту книгу?"):
            db.remove_book(self.book_id)
            self.deleteLater()

    @staticmethod
    def check_books(books):
        for book in books:
            if book.book_id in cart.get_books_ids():
                book.set_added()
            else:
                book.set_removed()

    def add_to_cart(self):
        if self.book_id not in cart.get_books_ids():
            cart.add_book(self.book_id, self.book_count)
            self.set_added()
        else:
            cart.remove_book(self.book_id)
            self.set_removed()

    def set_added(self):
        self.addCartBtn.setText("Убрать Из Корзины")
        self.addCartBtn.setStyleSheet('background-color: rgb(255, 0, 51);')

    def set_removed(self):
        self.addCartBtn.setText("Добавить В Корзину")
        self.addCartBtn.setStyleSheet('background-color: rgb(0, 153, 51);')

    def change_count(self):
        self.book_count = int(self.countSpinBox.value())
        cart.update_book(self.book_id, self.book_count)

    def set_count(self, book_count):
        self.book_count = book_count
        self.countSpinBox.setValue(book_count)
