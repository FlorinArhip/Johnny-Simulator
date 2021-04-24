# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QDialog


class Ui_ram_change_menu(object):
    def setupUi(self, ram_change_menu):
        ram_change_menu.setObjectName("ram_change_menu")
        ram_change_menu.setWindowModality(QtCore.Qt.NonModal)
        ram_change_menu.setEnabled(True)
        ram_change_menu.resize(518, 351)
        ram_change_menu.setMinimumSize(QtCore.QSize(518, 351))
        ram_change_menu.setMaximumSize(QtCore.QSize(518, 351))
        ram_change_menu.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label = QtWidgets.QLabel(ram_change_menu)
        self.label.setGeometry(QtCore.QRect(20, 20, 71, 21))
        self.label.setStyleSheet("font-size: 20px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(ram_change_menu)
        self.label_2.setGeometry(QtCore.QRect(160, 20, 61, 21))
        self.label_2.setStyleSheet("font-size: 20px;")
        self.label_2.setObjectName("label_2")
        self.adress_frame = QtWidgets.QFrame(ram_change_menu)
        self.adress_frame.setGeometry(QtCore.QRect(20, 60, 81, 81))
        self.adress_frame.setStyleSheet("#adress_frame{\n"
"background-color: rgb(203, 203, 203);\n"
"border-width: 1px;\n"
"border-style:solid;\n"
"}")
        self.adress_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.adress_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.adress_frame.setObjectName("adress_frame")
        self.adress_label = QtWidgets.QLabel(self.adress_frame)
        self.adress_label.setGeometry(QtCore.QRect(10, 20, 51, 31))
        self.adress_label.setStyleSheet("font-size: 20px;")
        self.adress_label.setObjectName("adress_label")
        self.data_frame = QtWidgets.QFrame(ram_change_menu)
        self.data_frame.setGeometry(QtCore.QRect(150, 60, 321, 81))
        self.data_frame.setStyleSheet("#data_frame{\n"
"background-color: rgb(203, 203, 203);\n"
"border-width: 1px;\n"
"border-style:solid;\n"
"}\n"
"")
        self.data_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.data_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.data_frame.setObjectName("data_frame")
        self.hi_text_edit = QtWidgets.QLineEdit(self.data_frame)
        self.hi_text_edit.setValidator(QtGui.QIntValidator())
        self.hi_text_edit.setGeometry(QtCore.QRect(30, 20, 51, 31))
        self.hi_text_edit.setObjectName("hi_text_edit")
        self.hi_text_edit.setStyleSheet("font-size:20px;")
        self.label_3 = QtWidgets.QLabel(self.data_frame)
        self.label_3.setGeometry(QtCore.QRect(30, 0, 47, 21))
        self.label_3.setStyleSheet("font-size:20px;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.data_frame)
        self.label_4.setGeometry(QtCore.QRect(150, 0, 47, 21))
        self.label_4.setStyleSheet("font-size:20px;")
        self.label_4.setObjectName("label_4")
        self.lo_text_edit = QtWidgets.QLineEdit(self.data_frame)
        self.lo_text_edit.setValidator(QtGui.QIntValidator())
        self.lo_text_edit.setGeometry(QtCore.QRect(150, 20, 51, 31))
        self.lo_text_edit.setObjectName("lo_text_edit")
        self.lo_text_edit.setStyleSheet("font-size:20px;")
        self.hi_selector = QtWidgets.QComboBox(self.data_frame)
        self.hi_selector.setGeometry(QtCore.QRect(30, 50, 69, 21))
        self.hi_selector.setCurrentText("")
        self.hi_selector.setObjectName("hi_selector")
        self.hi_lo_reset = QtWidgets.QPushButton(ram_change_menu)
        self.hi_lo_reset.setGeometry(QtCore.QRect(220, 180, 75, 41))
        self.hi_lo_reset.setStyleSheet("font-size:20px;")
        self.hi_lo_reset.setObjectName("hi_lo_reset")
        self.push_ram_info = QtWidgets.QPushButton(ram_change_menu)
        self.push_ram_info.setGeometry(QtCore.QRect(220, 230, 75, 41))
        self.push_ram_info.setStyleSheet("background-image: url(sprites/line_to_ram.png);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.push_ram_info.setText("")
        self.push_ram_info.setObjectName("push_ram_info")
        self.cancel_button = QtWidgets.QPushButton(ram_change_menu)
        self.cancel_button.setGeometry(QtCore.QRect(220, 280, 75, 41))
        self.cancel_button.setStyleSheet("font-size:18px;")
        self.cancel_button.setObjectName("cancel_button")

        self.retranslateUi(ram_change_menu)
        QtCore.QMetaObject.connectSlotsByName(ram_change_menu)

    def retranslateUi(self, ram_change_menu):
        _translate = QtCore.QCoreApplication.translate
        ram_change_menu.setWindowTitle(_translate("ram_change_menu", "Edit RAM Line"))
        self.label.setText(_translate("ram_change_menu", "Address"))
        self.label_2.setText(_translate("ram_change_menu", "Data"))
        self.adress_label.setText(_translate("ram_change_menu", "000:"))
        self.label_3.setText(_translate("ram_change_menu", "Hi"))
        self.label_4.setText(_translate("ram_change_menu", "Lo"))
        self.hi_lo_reset.setText(_translate("ram_change_menu", "00 000"))
        self.cancel_button.setText(_translate("ram_change_menu", "CANCEL"))

    
    def init(self):
        self.initHiLo()
        

    def initDropbox(self):
        self.dictionar = { "00: " : "00",
                                    "01: TAKE" : "01", 
                                    "02: ADD" : "02",
                                    "03: SUB" : "03",
                                    "04: SAVE" : "04",
                                    "05: JMP" : "05",
                                    "06: TST" : "06",
                                    "07: INC" : "07",
                                    "08: DEC" : "08",
                                    "09: NULL" : "09",
                                    "10: HLT" : "10"}
        self.hi_selector.addItems(self.dictionar)
        
    
    def buttonEventsInit(self):
        self.hi_selector.currentIndexChanged.connect(self.applyHiChoice)


    def applyHiChoice(self):
        index = self.dictionar[self.hi_selector.currentText()] 
        self.hi_text_edit.setText(index)
        
    def initHiLo(self):
        self.hi_text_edit.setText("00")
        self.lo_text_edit.setText("000")  


import sys

class Dialog(QDialog):
    def __init__(self):
        self.closed=0
        self.app = QtWidgets.QApplication(sys.argv)
        self.ram_change_menu = QtWidgets.QDialog()
        self.ui = Ui_ram_change_menu()
        self.ui.setupUi(self.ram_change_menu)
        self.ui.init()
        self.ui.initDropbox()
        self.ui.buttonEventsInit()
        self.ram_change_menu.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint )
    def close(self):
        self.ram_change_menu.close()
    
