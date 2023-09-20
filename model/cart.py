
class Cart:

    def __init__(self):
        self.books = []
        self.onAddCallbacks = []
        self.onRemoveCallbacks = []

    def add_book(self, book_id):
        self.books.append(book_id)

        for callback in self.onAddCallbacks:
            callback(book_id)

    def remove_book(self, book_id):
        self.books.remove(book_id)

        for callback in self.onRemoveCallbacks:
            callback(book_id)

    def get_books(self):
        return self.books

    def addOnAddCallback(self, callback):
        self.onAddCallbacks.append(callback)

    def addOnRemoveCallback(self, callback):
        self.onRemoveCallbacks.append(callback)

    def clear_cart(self):
        self.books.clear()

        for callback in self.onRemoveCallbacks:
            callback(-1)
