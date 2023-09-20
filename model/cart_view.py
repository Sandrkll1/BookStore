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

        self.backBtn.clicked.connect(self.go_back)
        self.price = 0

        cart.addOnAddCallback(self.add_book)
        cart.addOnRemoveCallback(self.remove_book)

        self.orderBtn.clicked.connect(self.go_order_placement)

    def load_cart(self):
        self.clear_products()

        books_cards = []

        for book_id in cart.get_books():
            book = db.get_book_by_id(book_id)
            book_card = BookCard(book[0], book[2], book[3], db.get_category_name(book[1]), book[4], book[5], book[7], self.main_window)
            books_cards.append(book_card)
            self.bookList.addWidget(book_card)

        BookCard.check_books(books_cards)

    def clear_products(self):
        layout = self.bookList.layout()  # Get the QVBoxLayout

        # Clear all child widgets from the QVBoxLayout
        for i in reversed(range(layout.count())):
            widget = layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def go_back(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)

    def add_book(self, book_id):
        self.calculate_total_price()

    def remove_book(self, book_id):
        self.calculate_total_price()

    def calculate_total_price(self):
        price = 0

        for book in cart.get_books():
            price += db.get_book_by_id(book)[6]

        self.price = price
        self.totalPrice.setText(f"Общая стоимость: {price} ₽")

    def set_user_id(self, user_id):
        self.current_user_id = user_id

    def go_order_placement(self):

        if len(cart.get_books()) == 0:
            show_error_message("Для оформления заказа нужно добавить желаемые товары в корзину.")
            return

        if self.main_window is not None:
            self.main_window.order_placement.set_total_price(self.price)
            self.main_window.order_placement.set_user_id(self.current_user_id)
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.order_placement)
