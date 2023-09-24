import sys
from PyQt5.QtWidgets import *

from model.add_book_view import AddBookView
from model.admin_panel import AdminPanel
from model.book_info_view import BookInfoView
from model.main_view import MainView
from model.order_details_view import OrderDetailsView
from model.order_placement import OrderPlacement
from model.registration import Registration
from model.authorization import Authorization
from model.cart_view import Cart
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
        self.cart = Cart(main_window=self)
        self.order_placement = OrderPlacement(main_window=self)
        self.admin_panel = AdminPanel(main_window=self)
        self.add_book_view = AddBookView(main_window=self)
        self.book_info_view = BookInfoView(main_window=self)
        self.orderDetailsView = OrderDetailsView(main_window=self)

        self.stacked_widget.addWidget(self.registration)
        self.stacked_widget.addWidget(self.authorization)
        self.stacked_widget.addWidget(self.mainMenu)
        self.stacked_widget.addWidget(self.cart)
        self.stacked_widget.addWidget(self.order_placement)
        self.stacked_widget.addWidget(self.admin_panel)
        self.stacked_widget.addWidget(self.add_book_view)
        self.stacked_widget.addWidget(self.book_info_view)
        self.stacked_widget.addWidget(self.orderDetailsView)

        # self.stacked_widget.setCurrentWidget(self.registration)
        # self.stacked_widget.setCurrentWidget(self.mainMenu)
        self.stacked_widget.setCurrentWidget(self.admin_panel)
        # self.stacked_widget.setCurrentWidget(self.add_book_view)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Main()
    window.show()
    sys.exit(app.exec_())
