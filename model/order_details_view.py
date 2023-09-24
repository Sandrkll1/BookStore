from PyQt5.QtWidgets import QMainWindow
from loader import db
from model.order_details_book_card import OrderDetailsBookCard
from design.layouts.order_details_layout import Ui_OrderDetails


class OrderDetailsView(QMainWindow, Ui_OrderDetails):

    def __init__(self, *args, main_window=None):
        super(OrderDetailsView, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.order_id = -1
        self.parent_window = None

        self.backBtn.clicked.connect(self.go_back)

    def set_order_id(self, order_id):
        self.order_id = order_id
        self.load_order_details()

    def set_parent_window(self, parent_window):
        self.parent_window = parent_window

    def load_order_details(self):

        if self.order_id == -1: return

        for item in db.get_order_items_by_order_id(self.order_id):
            book = db.get_book_by_id(item[2])
            if book is None: return

            quantity = item[3]
            book_card = OrderDetailsBookCard(book[0], book[2], book[3], db.get_category_name(book[1]), book[4], book[7], book[6], quantity, self.main_window, parent_window=self)
            self.booksLayout.addWidget(book_card)

    def clear_products(self):
        layout = self.booksLayout.layout()

        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def go_back(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.parent_window)
            self.clear_products()
