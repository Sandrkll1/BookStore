import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QListWidget, QListWidgetItem,
                             QVBoxLayout, QHBoxLayout, QScrollArea, QGridLayout, QPushButton)
from PyQt5.QtCore import Qt, QRect


class BookCard(QWidget):
    def __init__(self, title="Sample Book"):
        super().__init__()

        layout = QVBoxLayout()
        label = QLabel(title)
        button = QPushButton("Read More")

        layout.addWidget(label)
        layout.addWidget(button)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Bookstore")
        self.setGeometry(0, 0, 906, 724)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.mainLayout = QVBoxLayout(self.central_widget)

        # Title
        self.titleLabel = QLabel("Bookstore", self.central_widget)
        self.titleLabel.setStyleSheet("font: 36pt 'MS Shell Dlg 2';")
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.mainLayout.addWidget(self.titleLabel)

        # Container Layout
        self.containerLayout = QHBoxLayout()
        self.mainLayout.addLayout(self.containerLayout)

        # Left menu
        self.leftMenuLayout = QVBoxLayout()
        self.searchBar = QLineEdit(self.central_widget)
        self.searchBar.setPlaceholderText("Search books...")
        self.searchBar.setStyleSheet("font: 12pt 'MS Shell Dlg 2';")
        self.leftMenuLayout.addWidget(self.searchBar)

        self.categoriesList = QListWidget(self.central_widget)
        self.categoriesList.setStyleSheet("font: 14pt 'MS Shell Dlg 2';")
        items = ["Drama", "Fantasy", "Fairy-tail"]
        for item in items:
            self.categoriesList.addItem(QListWidgetItem(item))
        self.leftMenuLayout.addWidget(self.categoriesList)

        self.containerLayout.addLayout(self.leftMenuLayout)

        # Right scroll area
        self.productsScrollArea = QScrollArea(self.central_widget)
        self.productsScrollArea.setWidgetResizable(True)
        self.containerLayout.addWidget(self.productsScrollArea)

        self.productsContainer = QWidget(self.productsScrollArea)
        self.productsScrollArea.setWidget(self.productsContainer)
        self.productsGrid = QGridLayout(self.productsContainer)
        self.productsContainer.setLayout(self.productsGrid)

        self.book_card_width = 150
        self.resizeEvent = self.on_resize
        self.populate_books()

    def on_resize(self, event):
        self.populate_books()

    def populate_books(self):
        columns = self.productsScrollArea.width() // self.book_card_width

        # Удаляем все виджеты из сетки
        for i in reversed(range(self.productsGrid.count())):
            widget = self.productsGrid.itemAt(i).widget()
            widget.setParent(None)

        # Добавляем карточки книг
        books = [BookCard(f"Book {i}") for i in range(50)]
        for index, book_card in enumerate(books):
            try:
                row = index // columns
            except ZeroDivisionError:
                row = 0

            try:
                col = index % columns
            except ZeroDivisionError:
                col = 0
            self.productsGrid.addWidget(book_card, row, col)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
