# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UIforms/hotelReview.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1201, 636)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 571, 611))
        self.groupBox.setObjectName("groupBox")
        self.roomNumber = QtWidgets.QLineEdit(self.groupBox)
        self.roomNumber.setGeometry(QtCore.QRect(190, 40, 113, 26))
        self.roomNumber.setObjectName("roomNumber")
        self.addRoomBtn = QtWidgets.QPushButton(self.groupBox)
        self.addRoomBtn.setGeometry(QtCore.QRect(497, 40, 41, 26))
        self.addRoomBtn.setObjectName("addRoomBtn")
        self.roomTable = QtWidgets.QTableWidget(self.groupBox)
        self.roomTable.setGeometry(QtCore.QRect(30, 70, 511, 391))
        # self.roomTable.setSizeAdjustPolicy(QtCore.Qt.QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents)
        self.roomTable.setShowGrid(True)
        self.roomTable.setColumnCount(3)
        self.roomTable.setObjectName("roomTable")
        self.roomTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.roomTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.roomTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.roomTable.setHorizontalHeaderItem(2, item)
        self.delRoomBtn = QtWidgets.QPushButton(self.groupBox)
        self.delRoomBtn.setGeometry(QtCore.QRect(450, 40, 41, 26))
        self.delRoomBtn.setObjectName("delRoomBtn")
        self.roomReviewBtn = QtWidgets.QPushButton(self.groupBox)
        self.roomReviewBtn.setGeometry(QtCore.QRect(30, 40, 151, 26))
        self.roomReviewBtn.setObjectName("roomReviewBtn")
        self.roomNumInput = QtWidgets.QLineEdit(self.groupBox)
        self.roomNumInput.setGeometry(QtCore.QRect(30, 510, 111, 26))
        self.roomNumInput.setObjectName("roomNumInput")
        self.price = QtWidgets.QLineEdit(self.groupBox)
        self.price.setGeometry(QtCore.QRect(180, 510, 113, 26))
        self.price.setObjectName("price")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 480, 111, 18))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(180, 480, 66, 18))
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(610, 10, 571, 611))
        self.groupBox_2.setObjectName("groupBox_2")
        self.empNumber = QtWidgets.QLineEdit(self.groupBox_2)
        self.empNumber.setGeometry(QtCore.QRect(220, 40, 113, 26))
        self.empNumber.setObjectName("empNumber")
        self.addEmpBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.addEmpBtn.setGeometry(QtCore.QRect(497, 40, 41, 26))
        self.addEmpBtn.setObjectName("addEmpBtn")
        self.employersTable = QtWidgets.QTableWidget(self.groupBox_2)
        self.employersTable.setGeometry(QtCore.QRect(30, 70, 511, 391))
        # self.employersTable.setSizeAdjustPolicy(QtCore.Qt.QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents)
        self.employersTable.setShowGrid(True)
        self.employersTable.setColumnCount(3)
        self.employersTable.setObjectName("employersTable")
        self.employersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.employersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.employersTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.employersTable.setHorizontalHeaderItem(2, item)
        self.delEmpBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.delEmpBtn.setGeometry(QtCore.QRect(450, 40, 41, 26))
        self.delEmpBtn.setObjectName("delEmpBtn")
        self.empReviewBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.empReviewBtn.setGeometry(QtCore.QRect(30, 40, 181, 26))
        self.empReviewBtn.setObjectName("empReviewBtn")
        self.fio = QtWidgets.QLineEdit(self.groupBox_2)
        self.fio.setGeometry(QtCore.QRect(30, 510, 113, 26))
        self.fio.setObjectName("fio")
        self.salary = QtWidgets.QLineEdit(self.groupBox_2)
        self.salary.setGeometry(QtCore.QRect(270, 510, 113, 26))
        self.salary.setObjectName("salary")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(30, 480, 66, 18))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(150, 480, 91, 18))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(270, 480, 66, 18))
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setGeometry(QtCore.QRect(150, 510, 111, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Просмотр отеля"))
        self.groupBox.setTitle(_translate("Form", "Комнаты отеля"))
        self.addRoomBtn.setText(_translate("Form", "+"))
        item = self.roomTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "№ Комнаты"))
        item = self.roomTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ID Отеля"))
        item = self.roomTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Стоимость "))
        self.delRoomBtn.setText(_translate("Form", "-"))
        self.roomReviewBtn.setText(_translate("Form", "Просмотр комнаты"))
        self.label.setText(_translate("Form", "Номер комнаты"))
        self.label_2.setText(_translate("Form", "Цена"))
        self.groupBox_2.setTitle(_translate("Form", "Штат сотрудников"))
        self.addEmpBtn.setText(_translate("Form", "+"))
        item = self.employersTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ФИО"))
        item = self.employersTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Должность"))
        item = self.employersTable.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Оклад"))
        self.delEmpBtn.setText(_translate("Form", "-"))
        self.empReviewBtn.setText(_translate("Form", "Просмотр сотрудника"))
        self.label_3.setText(_translate("Form", "ФИО"))
        self.label_4.setText(_translate("Form", "Должность"))
        self.label_5.setText(_translate("Form", "Оклад"))
        self.comboBox.setItemText(0, _translate("Form", "Не выбрано"))
        self.comboBox.setItemText(1, _translate("Form", "Электрик"))
        self.comboBox.setItemText(2, _translate("Form", "Уборщик"))
        self.comboBox.setItemText(3, _translate("Form", "Администратор"))
