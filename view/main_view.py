from PyQt5.QtWidgets import *
from PyQt5 import uic
from .book_card import BookCard
from design.layouts.main_layout import Ui_MainWindow


class MainView(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(MainView, self).__init__(*args)
        # uic.loadUi(".\\layouts\\ui\\main_view.ui", self)
        #
        # self.main_window = main_window
        # self.current_user_id = current_user_id
        #
        # self.setMinimumSize(800, 600)
        #
        # self.containerLayout.setStretch(0, 1)
        # self.containerLayout.setStretch(1, 3)
        #
        # for i in range(10):
        #     self.productsVerticalLayout.addWidget(BookCard("jkdfjbsdfjkf", "jdshfhskf", "D:\\wallpapers\\pexels-photo-3131634.jpeg"))
        self.setupUi(self)

    def set_user_id(self, user_id):
        self.current_user_id = user_id
