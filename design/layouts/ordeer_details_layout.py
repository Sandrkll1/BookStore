# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\\design\\ui\\order_details.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OrderDetails(object):
    def setupUi(self, OrderDetails):
        OrderDetails.setObjectName("OrderDetails")
        OrderDetails.resize(816, 597)
        self.centralwidget = QtWidgets.QWidget(OrderDetails)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 377))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backBtn = QtWidgets.QPushButton(self.centralwidget)
        self.backBtn.setMinimumSize(QtCore.QSize(0, 30))
        self.backBtn.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout.addWidget(self.backBtn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 796, 530))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.booksLayout = QtWidgets.QVBoxLayout()
        self.booksLayout.setObjectName("booksLayout")
        self.verticalLayout_2.addLayout(self.booksLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        OrderDetails.setCentralWidget(self.centralwidget)

        self.retranslateUi(OrderDetails)
        QtCore.QMetaObject.connectSlotsByName(OrderDetails)

    def retranslateUi(self, OrderDetails):
        _translate = QtCore.QCoreApplication.translate
        OrderDetails.setWindowTitle(_translate("OrderDetails", "MainWindow"))
        self.backBtn.setText(_translate("OrderDetails", "Назад"))
        self.label.setText(_translate("OrderDetails", "Детали заказа"))
