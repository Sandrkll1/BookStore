import sys
from PyQt5.QtWidgets import *
import qdarkstyle
from design.layouts.registration_layout import Ui_MainWindow
from loader import db
from .helper import show_error_message


class Registration(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, main_window=None):
        super(Registration, self).__init__(*args)
        self.setupUi(self)

        self.main_window = main_window

        self.showPasswordCheckBox.stateChanged.connect(self.show_password)
        self.loginButton.clicked.connect(self.show_login)
        self.registerButton.clicked.connect(self.register)

    def show_password(self):
        if self.showPasswordCheckBox.isChecked():
            self.passwordEdit.setEchoMode(QLineEdit.Normal)
            self.repeatPasswordLineEdit.setEchoMode(QLineEdit.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.Password)
            self.repeatPasswordLineEdit.setEchoMode(QLineEdit.Password)

    def show_login(self):
        if self.main_window is not None:
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.authorization)

    def register(self):
        username = self.usernameEdit.text()
        password = self.passwordEdit.text()

        if len(username.strip()) == 0 or len(password.strip()) == 0:
            show_error_message("Пожалуйста, заполните все поля")
            return

        if len(password.strip()) <= 8:
            show_error_message("Пароль слишком короткий. Пароль должен содержать более 8 символов.")
            return

        if db.user_in_db(username):
            show_error_message("Пользователь с таким именем существует. Пожалуйста авторизуйтесь или введие другое имя.")

        else:
            db.add_user(username, password)
            self.main_window.mainMenu.set_user_id(db.get_user(username)[0])
            self.main_window.stacked_widget.setCurrentWidget(self.main_window.mainMenu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    window = Registration()
    window.show()
    sys.exit(app.exec_())
