
class Cart:

    def __init__(self):
        self.books = []
        self.onAddCallbacks = []
        self.onRemoveCallbacks = []
        self.onUpdateCallbacks = []

    def add_book(self, book_id, book_count=1):
        self.books.append([book_id, book_count])
        self.callOnAddEvent(book_id, book_count)

    def remove_book(self, book_id):
        for i in range(len(self.books)):
            if self.books[i][0] == book_id:
                self.books.pop(i)
                break

        self.callOnRemoveEvent(book_id)

    def update_book(self, book_id, book_count=1):
        for index, book in enumerate(self.books):
            if book[0] == book_id:
                self.books[index] = [book_id, book_count]
                break

        self.callOnUpdateEvent(book_id, book_count)

    def get_books(self):
        return self.books

    def get_books_ids(self):
        return [book[0] for book in self.books]

    def addOnAddCallback(self, callback):
        self.onAddCallbacks.append(callback)

    def addOnRemoveCallback(self, callback):
        self.onRemoveCallbacks.append(callback)

    def addOnUpdateCallback(self, callback):
        self.onUpdateCallbacks.append(callback)

    def clear_cart(self):
        self.books.clear()

        for callback in self.onRemoveCallbacks:
            callback(-1)

    def callOnAddEvent(self, book_id, book_count=1):
        for callback in self.onAddCallbacks:
            callback(book_id, book_count)

    def callOnRemoveEvent(self, book_id):
        for callback in self.onRemoveCallbacks:
            callback(book_id)

    def callOnUpdateEvent(self, book_id, book_count=1):
        for callback in self.onUpdateCallbacks:
            callback(book_id, book_count)
