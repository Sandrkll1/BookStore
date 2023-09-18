# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\\design\\ui\\book_card.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookCard(object):
    def setupUi(self, BookCard):
        BookCard.setObjectName("BookCard")
        BookCard.resize(873, 300)
        BookCard.setMaximumSize(QtCore.QSize(16777215, 300))
        self.horizontalLayout = QtWidgets.QHBoxLayout(BookCard)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bookImage = QtWidgets.QLabel(BookCard)
        self.bookImage.setMinimumSize(QtCore.QSize(200, 280))
        self.bookImage.setMaximumSize(QtCore.QSize(200, 280))
        self.bookImage.setObjectName("bookImage")
        self.horizontalLayout.addWidget(self.bookImage)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.bookTitle = QtWidgets.QLabel(BookCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookTitle.sizePolicy().hasHeightForWidth())
        self.bookTitle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.bookTitle.setFont(font)
        self.bookTitle.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.bookTitle.setTextFormat(QtCore.Qt.PlainText)
        self.bookTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bookTitle.setWordWrap(True)
        self.bookTitle.setObjectName("bookTitle")
        self.verticalLayout.addWidget(self.bookTitle)
        self.bookAuthor = QtWidgets.QLabel(BookCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookAuthor.sizePolicy().hasHeightForWidth())
        self.bookAuthor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookAuthor.setFont(font)
        self.bookAuthor.setWordWrap(True)
        self.bookAuthor.setObjectName("bookAuthor")
        self.verticalLayout.addWidget(self.bookAuthor)
        self.bookCategory = QtWidgets.QLabel(BookCard)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookCategory.setFont(font)
        self.bookCategory.setObjectName("bookCategory")
        self.verticalLayout.addWidget(self.bookCategory)
        self.bookYear = QtWidgets.QLabel(BookCard)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bookYear.setFont(font)
        self.bookYear.setObjectName("bookYear")
        self.verticalLayout.addWidget(self.bookYear)
        self.bookDescription = QtWidgets.QLabel(BookCard)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookDescription.sizePolicy().hasHeightForWidth())
        self.bookDescription.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.bookDescription.setFont(font)
        self.bookDescription.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.bookDescription.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bookDescription.setWordWrap(True)
        self.bookDescription.setObjectName("bookDescription")
        self.verticalLayout.addWidget(self.bookDescription)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_2 = QtWidgets.QPushButton(BookCard)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setAutoDefault(False)
        self.pushButton_2.setDefault(False)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(BookCard)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(BookCard)
        QtCore.QMetaObject.connectSlotsByName(BookCard)

    def retranslateUi(self, BookCard):
        _translate = QtCore.QCoreApplication.translate
        self.bookImage.setText(_translate("BookCard", "TextLabel"))
        self.bookTitle.setText(_translate("BookCard", "Book Title"))
        self.bookAuthor.setText(_translate("BookCard", "TextLabel"))
        self.bookCategory.setText(_translate("BookCard", "TextLabel"))
        self.bookYear.setText(_translate("BookCard", "TextLabel"))
        self.bookDescription.setText(_translate("BookCard", "Book description here..."))
        self.pushButton_2.setText(_translate("BookCard", "Узнать Больше"))
        self.pushButton.setText(_translate("BookCard", "Добавить В Корзину"))
