from PyQt5.QtWidgets import *
from PyQt5 import uic


class MainView(QMainWindow):

    def __init__(self, *args, main_window=None):
        super(MainView, self).__init__(*args)
        uic.loadUi(".\\design\\main_view.ui", self)

        self.main_window = main_window
        self.setMinimumSize(800, 600)

        with open(".\\styles\\main_view.qss", "r") as file:
            self.setStyleSheet(file.read())

        self.containerLayout.setStretch(0, 1)
        self.containerLayout.setStretch(1, 3)
        