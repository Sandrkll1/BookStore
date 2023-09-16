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

        self.load_books()

    def load_books(self):
        books = db.get_all_books()

        for book in books:
            book_card = BookCard(book[2], book[3], db.get_category_name(book[1]), book[4], book[5], book[7])
            self.productsVerticalLayout.addWidget(book_card)

    def set_user_id(self, user_id):
        self.current_user_id = user_id
