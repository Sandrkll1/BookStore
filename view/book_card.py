from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from design.layouts.book_card_layout import Ui_BookCard


class BookCard(QtWidgets.QWidget, Ui_BookCard):
    def __init__(self, title, author, category, year, description, image, parent=None):
        super(BookCard, self).__init__(parent)
        # uic.loadUi('.\\design\\ui\\book_card.ui', self)
        self.setupUi(self)

        self.bookTitle.setText(title)
        self.bookAuthor.setText(f"Автор: {author}")
        self.bookCategory.setText(f"Категория: {category}")
        self.bookYear.setText(f"Год издания: {year}")
        self.bookDescription.setText(description)

        if image is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.bookImage.setPixmap(pixmap)
            self.bookImage.setAlignment(Qt.AlignCenter)
            self.bookImage.setScaledContents(True)
