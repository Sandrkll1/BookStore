# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\\design\\ui\\admin_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(958, 708)
        self.centralwidget = QtWidgets.QWidget(AdminPanel)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.hboxlayout = QtWidgets.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setStyleSheet("font: 36pt \"MS Shell Dlg 2\";")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.hboxlayout.addWidget(self.titleLabel)
        self.mainLayout.addLayout(self.hboxlayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setStyleSheet("QTabWidget::pane {\n"
"       border-top: 3px solid #5a5a5a; /* Provides a border at the top of the content area */\n"
"   }\n"
"\n"
"   QTabBar::tab {\n"
"       border: 1px solid #aaa;    /* Border around each tab */\n"
"       border-bottom: none;       /* Remove the bottom border to merge with the content pane */\n"
"       border-top-left-radius: 10px;  /* Rounded top-left corner */\n"
"       border-top-right-radius: 10px; /* Rounded top-right corner */\n"
"       padding: 10px;             /* Space around the text */\n"
"       margin: 2px;               /* Space between tabs */\n"
"       margin-bottom: 0px;        /* Reduce bottom margin to let tabs touch the content pane */\n"
"       box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */\n"
"       transition: 0.3s;          /* Transition effect for smooth changes */\n"
"        font-size: 14pt;\n"
"        width: 100px;\n"
"        height: 15px;\n"
"   }\n"
"\n"
"   QTabBar::tab:selected {\n"
"       border-color: #555;       /* Darker border for the selected tab */\n"
"       box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15); /* Slightly more pronounced shadow for the selected tab */\n"
"   }\n"
"\n"
"\n"
"   QTabBar::tab:!selected {\n"
"       margin-top: 3px;            /* Unselected tabs are slightly lower */\n"
"       box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05); /* Subtle shadow for unselected tabs */\n"
"   }")
        self.tabWidget.setObjectName("tabWidget")
        self.booksTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.booksTab.setFont(font)
        self.booksTab.setObjectName("booksTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.booksTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.searchBar = QtWidgets.QLineEdit(self.booksTab)
        self.searchBar.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; padding: 10px; border: 2px solid #aaa; border-radius: 5px;")
        self.searchBar.setObjectName("searchBar")
        self.verticalLayout_2.addWidget(self.searchBar)
        self.booksScrollArea = QtWidgets.QScrollArea(self.booksTab)
        self.booksScrollArea.setWidgetResizable(True)
        self.booksScrollArea.setAlignment(QtCore.Qt.AlignJustify|QtCore.Qt.AlignVCenter)
        self.booksScrollArea.setObjectName("booksScrollArea")
        self.booksContainer = QtWidgets.QWidget()
        self.booksContainer.setGeometry(QtCore.QRect(0, 0, 920, 469))
        self.booksContainer.setObjectName("booksContainer")
        self.productsVerticalLayout = QtWidgets.QVBoxLayout(self.booksContainer)
        self.productsVerticalLayout.setSpacing(10)
        self.productsVerticalLayout.setObjectName("productsVerticalLayout")
        self.booksLayout = QtWidgets.QVBoxLayout()
        self.booksLayout.setObjectName("booksLayout")
        self.productsVerticalLayout.addLayout(self.booksLayout)
        self.booksScrollArea.setWidget(self.booksContainer)
        self.verticalLayout_2.addWidget(self.booksScrollArea)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exitAccountBtn = QtWidgets.QPushButton(self.booksTab)
        self.exitAccountBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.exitAccountBtn.setMaximumSize(QtCore.QSize(150, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.exitAccountBtn.setFont(font)
        self.exitAccountBtn.setObjectName("exitAccountBtn")
        self.horizontalLayout.addWidget(self.exitAccountBtn, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.addBookBtn = QtWidgets.QPushButton(self.booksTab)
        self.addBookBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.addBookBtn.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBookBtn.setFont(font)
        self.addBookBtn.setObjectName("addBookBtn")
        self.horizontalLayout.addWidget(self.addBookBtn, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tabWidget.addTab(self.booksTab, "")
        self.orderTab = QtWidgets.QWidget()
        self.orderTab.setObjectName("orderTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.orderTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.orderSearchBar = QtWidgets.QLineEdit(self.orderTab)
        self.orderSearchBar.setStyleSheet("font: 14pt \"MS Shell Dlg 2\"; padding: 10px; border: 2px solid #aaa; border-radius: 5px;")
        self.orderSearchBar.setObjectName("orderSearchBar")
        self.verticalLayout_3.addWidget(self.orderSearchBar, 0, QtCore.Qt.AlignTop)
        self.ordersScrollArea = QtWidgets.QScrollArea(self.orderTab)
        self.ordersScrollArea.setWidgetResizable(True)
        self.ordersScrollArea.setObjectName("ordersScrollArea")
        self.ordersContainer = QtWidgets.QWidget()
        self.ordersContainer.setGeometry(QtCore.QRect(0, 0, 920, 528))
        self.ordersContainer.setObjectName("ordersContainer")
        self.ordersContainerLayout = QtWidgets.QVBoxLayout(self.ordersContainer)
        self.ordersContainerLayout.setSpacing(10)
        self.ordersContainerLayout.setObjectName("ordersContainerLayout")
        self.ordersLayout = QtWidgets.QVBoxLayout()
        self.ordersLayout.setObjectName("ordersLayout")
        self.ordersContainerLayout.addLayout(self.ordersLayout)
        self.ordersScrollArea.setWidget(self.ordersContainer)
        self.verticalLayout_3.addWidget(self.ordersScrollArea)
        self.tabWidget.addTab(self.orderTab, "")
        self.mainLayout.addWidget(self.tabWidget)
        AdminPanel.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminPanel)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "Admin Panel - Bookstore"))
        self.titleLabel.setText(_translate("AdminPanel", "Admin Panel"))
        self.searchBar.setPlaceholderText(_translate("AdminPanel", "Поиск книг..."))
        self.exitAccountBtn.setText(_translate("AdminPanel", "Выйти с аккаунта"))
        self.addBookBtn.setText(_translate("AdminPanel", "Добавить книгу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.booksTab), _translate("AdminPanel", "Книги"))
        self.orderSearchBar.setPlaceholderText(_translate("AdminPanel", "ID Пользователя..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.orderTab), _translate("AdminPanel", "Заказы"))
