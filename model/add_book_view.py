from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QFileDialog
from .helper import show_error_message, show_question_message
from design.layouts.add_book_layout import Ui_BookAddMainWindow
from loader import default_image, db


# pyuic5 -o .\\design\\layouts\\add_book_layout.py .\\design\\ui\\add_book_view.ui
class AddBookView(QtWidgets.QMainWindow, Ui_BookAddMainWindow):

    def __init__(self, *args, main_window=None):
        super(AddBookView, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.coverPath = None

        pixmap = QPixmap()
        pixmap.loadFromData(default_image)
        self.coverLabel.setPixmap(pixmap)
        self.coverLabel.setAlignment(Qt.AlignCenter)
        self.coverLabel.setScaledContents(True)

        self.addBookButton.clicked.connect(self.addBook)
        self.chooseCoverButton.clicked.connect(self.chooseCover)
        self.backBtn.clicked.connect(self.back)

        self.load_categories()

    def load_categories(self):
        self.categoryComboBox.addItems([category[1] for category in db.get_all_categories()])

    def get_name(self):
        return self.bookNameLineEdit.text()

    def get_author(self):
        return self.authorLineEdit.text()

    def get_year(self):
        return int(self.yearSpinBox.value())

    def get_description(self):
        return self.descriptionTextEdit.toPlainText()

    def get_price(self):
        return float(self.priceDoubleSpinBox.value())

    def chooseCover(self):
        file_dialog = QFileDialog(self)
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter('Pictures (*.png *.jpg *.jpeg *.bmp)')

        if file_dialog.exec_():
            self.coverPath = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(self.coverPath)
            self.coverLabel.setPixmap(pixmap)

    def addBook(self):
        name = self.get_name()
        author = self.get_author()
        year = self.get_year()
        description = self.get_description()
        price = self.get_price()

        if not name.strip():
            show_error_message("Пожалуйста, введите название книги.")
            return

        if not author.strip():
            show_error_message("Пожалуйста, введите автора книги.")
            return

        if year == 0:
            show_error_message("Пожалуйста, введите год выпуска книги.")
            return

        if not description.strip():
            show_error_message("Пожалуйста, введите описание книги.")
            return

        if price <= 0:
            show_error_message("Пожалуйста, введите корректную цену книги.")
            return

        if show_question_message("Вы уверены что хотитке добавить книгу?"):
            category_id = db.get_category_id(self.categoryComboBox.currentText())
            db.add_book(name, author, year, description, price, category_id, self.coverPath)

            if self.main_window is not None:
                self.main_window.admin_panel.clear_products()
                self.main_window.admin_panel.load_books()
                self.main_window.stacked_widget.setCurrentWidget(self.main_window.admin_panel)
                self.clear_all_fields()

    def back(self):
        if show_question_message("Вы точно хотите выйти?"):
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.admin_panel)

    def clear_all_fields(self):
        """Clear all input fields."""
        self.bookNameLineEdit.clear()
        self.authorLineEdit.clear()
        self.yearSpinBox.setValue(0)
        self.descriptionTextEdit.clear()
        self.priceDoubleSpinBox.setValue(self.priceDoubleSpinBox.minimum())
        pixmap = QPixmap()
        pixmap.loadFromData(default_image)
        self.coverLabel.setPixmap(pixmap)
        self.coverPath = None
