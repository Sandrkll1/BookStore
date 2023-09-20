from PyQt5.QtWidgets import QMessageBox


def show_error_message(message):
    error_dialog = QMessageBox()
    error_dialog.setWindowTitle("Ошибка")
    error_dialog.setIcon(QMessageBox.Critical)
    error_dialog.setText(message)
    error_dialog.setStandardButtons(QMessageBox.Ok)

    error_dialog.setStyleSheet("""
        QMessageBox {
            background-color: #F9EBE0;
            font-size: 16px;
            color: #D43F00;
            border: 2px solid #D43F00;
            border-radius: 5px;
        }
        QMessageBox QLabel {
            background-color: transparent;
            color: #000000;
        }
        QMessageBox QPushButton {
            background-color: #D43F00;
            color: #FFFFFF;
            padding: 10px;
            border-radius: 3px;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background-color: #BF360C;
        }
    """)

    error_dialog.exec_()


def show_success_message(message):
    success_dialog = QMessageBox()
    success_dialog.setWindowTitle("Успех")
    success_dialog.setIcon(QMessageBox.Information)
    success_dialog.setText(message)
    success_dialog.setStandardButtons(QMessageBox.Ok)

    success_dialog.setStyleSheet("""
        QMessageBox {
            background-color: transparent;
            font-size: 16px;
            color: #004d40;  # Зеленый цвет текста
            border: 2px solid #4CAF50;  # Зеленый цвет рамки
            border-radius: 5px;
        }
        QMessageBox QLabel {
            background-color: transparent;
        }
        QMessageBox QPushButton {
            background-color: #4CAF50;  # Зеленый цвет кнопки
            color: #FFFFFF;
            padding: 10px;
            border-radius: 3px;
            min-width: 80px;
        }
        QMessageBox QPushButton:hover {
            background-color: #388E3C;  # Темнее зеленый при наведении
        }
    """)

    success_dialog.exec_()
