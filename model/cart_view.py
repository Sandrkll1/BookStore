from PyQt5.QtWidgets import *
from loader import db, cart
from model.book_card import BookCard
from design.layouts.cart_layout import Ui_BookStoreCart
from .helper import show_error_message


class Cart(QMainWindow, Ui_BookStoreCart):

    def __init__(self, *args, main_window=None, current_user_id=-1):
        super(Cart, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window
        self.current_user_id = current_user_id
        self.price = 0

        cart.addOnAddCallback(self.on_add_remove_book)
        cart.addOnRemoveCallback(self.on_add_remove_book)
        cart.addOnUpdateCallback(self.update_book_count)

        self.backBtn.clicked.connect(self.go_back)
        self.orderBtn.clicked.connect(self.go_order_placement)

    def load_cart(self):
        self.clear_products()

        book_cards = []

        for _book in cart.get_books():
            book = self.get_book_by_id(_book[0])
            book_card = BookCard(
                book[0], book[2], book[3], self.get_category_name(book[1]),
                book[4], book[5], book[7], book[6], main_window=self.main_window, parent_window=self
            )
            book_card.set_count(_book[1])
            book_cards.append(book_card)
            self.bookList.addWidget(book_card)

        BookCard.check_books(book_cards)

    @staticmethod
    def get_book_by_id(book_id):
        return db.get_book_by_id(book_id)

    @staticmethod
    def get_category_name(category_id):
        return db.get_category_name(category_id)

    def clear_products(self):
        layout = self.bookList.layout()
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def go_back(self):
        if self.main_window:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)

    def on_add_remove_book(self, *args):
        self.clear_products()
        self.load_cart()
        self.calculate_total_price()

    def calculate_total_price(self, *args):
        price = 0
        for book in cart.get_books():
            price += self.get_book_by_id(book[0])[6] * book[1]
        self.price = price
        self.totalPrice.setText(f"Общая стоимость: {price} ₽")

    def update_book_count(self, book_id, book_count):
        layout = self.bookList.layout()
        for i in range(layout.count()):
            widget = layout.itemAt(i).widget()
            if widget and isinstance(widget, BookCard) and (widget.book_id == book_id or book_id == -1):
                widget.set_count(book_count)
        self.calculate_total_price()

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def go_order_placement(self):
        if not cart.get_books():
            show_error_message("Для оформления заказа нужно добавить желаемые товары в корзину.")
            return
        if self.main_window:
            self.main_window.order_placement.set_total_price(self.price)
            self.main_window.order_placement.set_user_id(self.current_user_id)
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.order_placement)
