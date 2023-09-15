import sys
from PyQt5.QtWidgets import *
from view.main_view import MainView
from view.registration import Registration
from view.authorization import Authorization
import qdarkstyle


class Main(QMainWindow):

    def __init__(self, *args):
        super(Main, self).__init__(*args)
        self.setMinimumWidth(800)
        self.setMinimumHeight(600)

        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        self.registration = Registration(main_window=self)
        self.authorization = Authorization(main_window=self)
        self.mainMenu = MainView(main_window=self)

        self.stacked_widget.addWidget(self.registration)
        self.stacked_widget.addWidget(self.authorization)
        self.stacked_widget.addWidget(self.mainMenu)

        self.stacked_widget.setCurrentWidget(self.registration)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()
    window.show()
    sys.exit(app.exec_())
