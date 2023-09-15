from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap


class BookCard(QtWidgets.QWidget):
    def __init__(self, title, description, image_path, parent=None):
        super(BookCard, self).__init__(parent)
        uic.loadUi('.\\design\\ui\\book_card.ui', self)

        self.bookTitle.setText(title)
        self.bookDescription.setText(description)
        self.bookImage.setPixmap(QPixmap(image_path))
