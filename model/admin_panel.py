from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QMainWindow
from loader import db
from model.book_card import BookCard
from model.order_card import OrderCard
from design.layouts.admin_layout import Ui_AdminPanel
from .helper import show_question_message


class AdminPanel(QMainWindow, Ui_AdminPanel):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(AdminPanel, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id

        self.load_books()
        self.load_orders()

        self.searchBar.textChanged.connect(self.search_books)
        self.orderSearchBar.textChanged.connect(self.search_orders)
        self.orderSearchBar.setValidator(QIntValidator())
        self.addBookBtn.clicked.connect(self.add_book)

        self.exitAccountBtn.clicked.connect(self.exit_account)

    def set_user_id(self, user_id):
        self.current_user_id = user_id
        self.clear_orders()
        self.load_orders()

    def load_books(self, books=None):
        if books is None:
            books = db.get_all_books()

        books_cards = []

        for book in books:
            book_card = BookCard(book[0], book[2], book[3], db.get_category_name(book[1]), book[4], book[5], book[7], book[6], True, self.main_window, parent_window=self)
            books_cards.append(book_card)
            self.booksLayout.addWidget(book_card)

        BookCard.check_books(books_cards)

    def load_orders(self, orders=None):

        if orders is None:
            orders = db.get_all_orders()

        for order in orders:
            order_card = OrderCard(order[0], order[1], order[6], order[2], order[3], order[4], order[5], main_window=self.main_window, parent_window=self)
            self.ordersLayout.addWidget(order_card)

    def clear_products(self):
        layout = self.booksLayout.layout()

        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def clear_orders(self):
        layout = self.ordersLayout.layout()

        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def search_books(self):
        text = self.searchBar.text()
        books = None

        if len(text.strip()) != 0:
            books = db.search_books_name(self.searchBar.text())

        self.clear_products()
        self.load_books(books)

    def search_orders(self):
        text = self.orderSearchBar.text()

        orders = None

        if len(text.strip()) != 0:
            orders = db.get_orders_by_user(int(self.orderSearchBar.text()))

        self.clear_orders()
        self.load_orders(orders)

    def add_book(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.add_book_view)

    def exit_account(self):
        if show_question_message("Вы точно хотите выйти с аккаунта?"):
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.authorization)