from PyQt5.QtWidgets import *
from PyQt5 import uic


class MainView(QMainWindow):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(MainView, self).__init__(*args)
        uic.loadUi(".\\design\\main_view.ui", self)

        self.main_window = main_window
        self.current_user_id = current_user_id

        self.setMinimumSize(800, 600)

        self.containerLayout.setStretch(0, 1)
        self.containerLayout.setStretch(1, 3)

    def set_user_id(self, user_id):
        self.current_user_id = user_id
