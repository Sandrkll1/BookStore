from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from design.layouts.book_card_layout import Ui_BookCard


class OrderDetailsBookCard(QtWidgets.QWidget, Ui_BookCard):

    def __init__(self, book_id, title, author, category, year, image, price=0, quantity=1, main_window=None, parent=None, parent_window=None):
        super(OrderDetailsBookCard, self).__init__(parent)
        self.setupUi(self)

        self.book_id = book_id
        self.main_window = main_window
        self.parent_window = parent_window

        self.bookTitle.setText(title)
        self.bookAuthor.setText(f"Автор: {author}")
        self.bookCategory.setText(f"Категория: {category}")
        self.bookYear.setText(f"Год издания: {year}")
        self.bookPrice.setText(f"Цена: {price}")
        self.countSpinBox.setValue(int(quantity))
        self.countSpinBox.setReadOnly(True)

        if image is not None:
            pixmap = QPixmap()
            pixmap.loadFromData(image)
            self.bookImage.setPixmap(pixmap)
            self.bookImage.setAlignment(Qt.AlignCenter)
            self.bookImage.setScaledContents(True)

        self.addCartBtn.hide()
        self.infoBtn.clicked.connect(self.show_book_info)

    def show_book_info(self):
        if self.main_window is not None:
            self.main_window.book_info_view.set_last_window(self.parent_window)
            self.main_window.book_info_view.set_book_id(self.book_id)
            self.main_window.book_info_view.set_is_admin(True)
            self.main_window.book_info_view.set_parent_window(self)
            self.main_window.book_info_view.hide_buttons()
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.book_info_view)