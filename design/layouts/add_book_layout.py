# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\\design\\ui\\add_book_view.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BookAddMainWindow(object):
    def setupUi(self, BookAddMainWindow):
        BookAddMainWindow.setObjectName("BookAddMainWindow")
        BookAddMainWindow.resize(947, 784)
        self.centralWidget = QtWidgets.QWidget(BookAddMainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.mainVerticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.mainVerticalLayout.setContentsMargins(20, 20, 20, 20)
        self.mainVerticalLayout.setSpacing(20)
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        self.mainTitleLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.mainTitleLabel.setFont(font)
        self.mainTitleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.mainTitleLabel.setObjectName("mainTitleLabel")
        self.mainVerticalLayout.addWidget(self.mainTitleLabel)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(25)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.coverLabel = QtWidgets.QLabel(self.centralWidget)
        self.coverLabel.setMaximumSize(QtCore.QSize(300, 450))
        self.coverLabel.setObjectName("coverLabel")
        self.verticalLayout_6.addWidget(self.coverLabel, 0, QtCore.Qt.AlignHCenter)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_6)
        self.bookNameLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bookNameLabel.setFont(font)
        self.bookNameLabel.setObjectName("bookNameLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.bookNameLabel)
        self.bookNameLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.bookNameLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bookNameLineEdit.setFont(font)
        self.bookNameLineEdit.setObjectName("bookNameLineEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bookNameLineEdit)
        self.authorLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.authorLabel)
        self.authorLineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.authorLineEdit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.authorLineEdit.setFont(font)
        self.authorLineEdit.setObjectName("authorLineEdit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.authorLineEdit)
        self.categoryLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setObjectName("categoryLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.categoryLabel)
        self.categoryComboBox = QtWidgets.QComboBox(self.centralWidget)
        self.categoryComboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.categoryComboBox.setFont(font)
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.categoryComboBox)
        self.yearLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yearLabel.setFont(font)
        self.yearLabel.setObjectName("yearLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.yearLabel)
        self.yearSpinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.yearSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.yearSpinBox.setFont(font)
        self.yearSpinBox.setMinimum(-1000)
        self.yearSpinBox.setMaximum(2099)
        self.yearSpinBox.setObjectName("yearSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.yearSpinBox)
        self.descriptionLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descriptionLabel.setFont(font)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.descriptionLabel)
        self.descriptionTextEdit = QtWidgets.QTextEdit(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.descriptionTextEdit.setFont(font)
        self.descriptionTextEdit.setObjectName("descriptionTextEdit")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.descriptionTextEdit)
        self.priceLabel = QtWidgets.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceLabel.setFont(font)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
        self.priceDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.priceDoubleSpinBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.priceDoubleSpinBox.setFont(font)
        self.priceDoubleSpinBox.setDecimals(2)
        self.priceDoubleSpinBox.setMaximum(9999.99)
        self.priceDoubleSpinBox.setObjectName("priceDoubleSpinBox")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.priceDoubleSpinBox)
        self.mainVerticalLayout.addLayout(self.formLayout)
        self.bottomHorizontalLayout = QtWidgets.QHBoxLayout()
        self.bottomHorizontalLayout.setSpacing(15)
        self.bottomHorizontalLayout.setObjectName("bottomHorizontalLayout")
        self.backBtn = QtWidgets.QPushButton(self.centralWidget)
        self.backBtn.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.bottomHorizontalLayout.addWidget(self.backBtn)
        self.chooseCoverButton = QtWidgets.QPushButton(self.centralWidget)
        self.chooseCoverButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.chooseCoverButton.setFont(font)
        self.chooseCoverButton.setFlat(True)
        self.chooseCoverButton.setObjectName("chooseCoverButton")
        self.bottomHorizontalLayout.addWidget(self.chooseCoverButton)
        self.addBookButton = QtWidgets.QPushButton(self.centralWidget)
        self.addBookButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.addBookButton.setFont(font)
        self.addBookButton.setFlat(True)
        self.addBookButton.setObjectName("addBookButton")
        self.bottomHorizontalLayout.addWidget(self.addBookButton)
        self.mainVerticalLayout.addLayout(self.bottomHorizontalLayout)
        BookAddMainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(BookAddMainWindow)
        QtCore.QMetaObject.connectSlotsByName(BookAddMainWindow)

    def retranslateUi(self, BookAddMainWindow):
        _translate = QtCore.QCoreApplication.translate
        BookAddMainWindow.setWindowTitle(_translate("BookAddMainWindow", "Add Book to BookStore"))
        self.mainTitleLabel.setText(_translate("BookAddMainWindow", "Добавить книгу"))
        self.coverLabel.setText(_translate("BookAddMainWindow", "TextLabel"))
        self.bookNameLabel.setText(_translate("BookAddMainWindow", "Название"))
        self.authorLabel.setText(_translate("BookAddMainWindow", "Автор"))
        self.categoryLabel.setText(_translate("BookAddMainWindow", "Категория"))
        self.yearLabel.setText(_translate("BookAddMainWindow", "Год издания"))
        self.descriptionLabel.setText(_translate("BookAddMainWindow", "Описание"))
        self.priceLabel.setText(_translate("BookAddMainWindow", "Цена"))
        self.backBtn.setText(_translate("BookAddMainWindow", "Назад"))
        self.chooseCoverButton.setText(_translate("BookAddMainWindow", "Выбрать обложку"))
        self.addBookButton.setText(_translate("BookAddMainWindow", "Добавить книгу"))
