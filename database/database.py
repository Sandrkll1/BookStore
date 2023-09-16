import os.path
import sqlite3


class BaseDatabase:

    def __init__(self, filename):
        self.filename = filename
        self.db = sqlite3.connect(filename)
        self.cursor = self.db.cursor()

    @staticmethod
    def convert_to_binary_data(filename):
        with open(filename, 'rb') as file:
            blob_data = file.read()
        return blob_data


class UserDatabase(BaseDatabase):

    def __init__(self, filename):
        super().__init__(filename)
        self.create_table()

    def create_table(self):
        query = """
                   CREATE TABLE IF NOT EXISTS users(
                       user_id          INTEGER PRIMARY KEY AUTOINCREMENT,
                       username         VARCHAR(60),
                       password         VARCHAR(60), 
                       is_admin         BOOLEAN DEFAULT FALSE
                   ); 
                   """

        self.cursor.execute(query)
        self.db.commit()

    def add_user(self, username, password, is_admin=False):
        self.cursor.execute("""INSERT INTO users (username, password, is_admin) VALUES(?, ?, ?)""", (username, password, is_admin,))
        self.db.commit()

    def get_user(self, username) -> tuple:
        user = self.cursor.execute("""SELECT * FROM users WHERE username = ?""", (username,))
        return user.fetchone()

    def get_user_by_id(self, user_id):
        user = self.cursor.execute("""SELECT * FROM users WHERE user_id =?""", (user_id,))
        return user.fetchone()

    def user_in_db(self, username) -> bool:
        return bool(self.get_user(username))

    def check_user(self, username, password) -> bool:
        user = self.cursor.execute("""SELECT * FROM users WHERE username = ? AND password = ?""", (username, password,))
        return bool(len(user.fetchall()))

    def is_admin(self, username, password=None) -> bool:
        if password is not None:
            user = self.cursor.execute("""SELECT is_admin FROM users WHERE username = ? AND password = ?""", (username, password,))
            return user.fetchone()[0]
        else:
            user = self.cursor.execute("""SELECT is_admin FROM users WHERE username = ?""", (password,))
            return user.fetchone()[0]


class CategoryDatabase(BaseDatabase):

    def __init__(self, filename):
        super().__init__(filename)
        self.create_table()

    def create_table(self):
        query = """
                   CREATE TABLE IF NOT EXISTS categories(
                       category_id          INTEGER PRIMARY KEY AUTOINCREMENT,
                       category_name        TEXT
                   ); 
                   """

        self.cursor.execute(query)
        self.db.commit()

    def get_category_name(self, category_id):
        category_name = self.cursor.execute("""SELECT * FROM categories WHERE category_id = ?""", (category_id, ))
        return category_name.fetchone()[1]

    def get_category_id(self, category_name):
        category_id = self.cursor.execute("""SELECT * FROM categories WHERE category_name = ?""", (category_name, ))
        return category_id.fetchone()[0]

    def add_category(self, category_name):
        self.cursor.execute("""INSERT INTO categories(category_name) VALUES(?)""", (category_name, ))
        self.db.commit()


class BookDatabase(BaseDatabase):

    def __init__(self, filename):
        super().__init__(filename)
        self.create_table()

    def create_table(self):
        query = """
                   CREATE TABLE IF NOT EXISTS books(
                       book_id          INTEGER PRIMARY KEY AUTOINCREMENT,
                       category_id      INTEGER,
                       book_name        TEXT,
                       author           VARCHAR(60), 
                       year             INTEGER,
                       description      TEXT,
                       price            DOUBLE,
                       cover            BLOB,
                       FOREIGN KEY (category_id) REFERENCES categories(category_id)
                   ); 
                   """

        self.cursor.execute(query)
        self.db.commit()

    def add_book(self, book_name, author, year, description, price, category_id, cover=None):
        if cover is not None and os.path.isfile(cover):
            cover = self.convert_to_binary_data(cover)

        self.cursor.execute("""INSERT INTO books(book_name, author, year, description, price, category_id, cover) VALUES(?, ?, ?, ?, ?, ?, ?)""",
                            (book_name, author, year, description, price, category_id, cover, ))
        self.db.commit()

    def get_book_by_id(self, book_id):
        book = self.cursor.execute("""SELECT * FROM books WHERE book_id = ?""", (book_id,))
        return book.fetchone()

    def get_book_by_name(self, book_name):
        book = self.cursor.execute("""SELECT * FROM books WHERE book_name = ?""", (book_name,))
        return book.fetchone()

    def get_all_books(self):
        books = self.cursor.execute("""SELECT * FROM books""")
        return books.fetchall()


class OrderDatabase(BaseDatabase):

    def __init__(self, filename):
        super().__init__(filename)
        self.create_table()

    def create_table(self):
        query = """
                   CREATE TABLE IF NOT EXISTS orders(
                       order_id         INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id          INTEGER,
                       book_id          INTEGER,
                       price            DOUBLE,
                       address          VARCHAR(90),
                       FOREIGN KEY (user_id) REFERENCES users(user_id),
                       FOREIGN KEY (book_id) REFERENCES books(book_id)  
                   ); 
                   """

        self.cursor.execute(query)
        self.db.commit()

    def add_order(self, user_id, book_id, price, address):
        self.cursor.execute("""INSERT INTO orders(user_id, book_id, price, address) VALUES(?, ?, ?, ?)""", (user_id, book_id, price, address))
        self.db.commit()

    def get_order_by_id(self, order_id):
        order = self.cursor.execute("""SELECT * FROM orders WHERE order_id = ?""", (order_id,))
        return order.fetchone()

    def get_orders_by_user(self, user_id):
        orders = self.cursor.execute("""SELECT * FROM orders WHERE user_id = ?""", (user_id,))
        return orders.fetchall()


class Database(UserDatabase, CategoryDatabase, BookDatabase, OrderDatabase):
    def __init__(self, filename):
        super().__init__(filename)
        CategoryDatabase.create_table(self)
        BookDatabase.create_table(self)
        OrderDatabase.create_table(self)


if __name__ == "__main__":
    db = Database(".\\test.db")
