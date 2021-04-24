# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProiectASC_UI.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem, QAbstractItemView, QMessageBox, QFileDialog
import Dialog_UI


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1010, 755)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1010, 755))
        MainWindow.setMaximumSize(QtCore.QSize(1010, 755))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(0, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(9999, 9999))
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.background_image = QtWidgets.QFrame(self.centralwidget)
        self.background_image.setGeometry(QtCore.QRect(0, 70, 1011, 681))
        self.background_image.setAutoFillBackground(False)
        self.background_image.setStyleSheet("QWidget #background_image\n"
                                            "{\n"
                                            "border-image: url(sprites/Hintergrund.png) 0 0 0 0 stretch stretch;\n"
                                            "}\n"
                                            "")
        self.background_image.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.background_image.setFrameShadow(QtWidgets.QFrame.Raised)
        self.background_image.setObjectName("background_image")
        self.cat_img = QtWidgets.QFrame(self.centralwidget)
        self.cat_img.setGeometry(QtCore.QRect(290, 120, 481, 601))
        self.cat_img.setStyleSheet("image: url(sprites/guido_mirror.png);\n"
                                   "background-color: rgb(193, 193, 193);\n"
                                   "border-style:solid;\n"
                                   "border-width:3px;")
        self.cat_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cat_img.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cat_img.setObjectName("cat_img")
        self.ram_address_set = QtWidgets.QPushButton(self.background_image)
        self.ram_address_set.setGeometry(QtCore.QRect(110, 20, 21, 71))
        self.ram_address_set.setText("")
        self.ram_address_set.setObjectName("ram_address_set")
        self.ram_address_setter = QtWidgets.QTextEdit(self.background_image)
        self.ram_address_setter.setGeometry(QtCore.QRect(40, 40, 71, 31))
        self.ram_address_setter.setStyleSheet("font-size: 20px;")
        self.ram_address_setter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ram_address_setter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ram_address_setter.setObjectName("ram_address_setter")
        self.ram_position = QtWidgets.QLabel(self.background_image)
        self.ram_position.setGeometry(QtCore.QRect(150, 110, 101, 41))
        self.ram_position.setStyleSheet("font-size: 30px;")
        self.ram_position.setTextFormat(QtCore.Qt.AutoText)
        self.ram_position.setScaledContents(False)
        self.ram_position.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_position.setObjectName("ram_position")
        self.address_bus = QtWidgets.QLabel(self.background_image)
        self.address_bus.setGeometry(QtCore.QRect(390, 40, 101, 41))
        self.address_bus.setStyleSheet("font-size: 30px;")
        self.address_bus.setTextFormat(QtCore.Qt.AutoText)
        self.address_bus.setScaledContents(False)
        self.address_bus.setAlignment(QtCore.Qt.AlignCenter)
        self.address_bus.setObjectName("address_bus")
        self.ram_lo = QtWidgets.QLabel(self.background_image)
        self.ram_lo.setGeometry(QtCore.QRect(190, 490, 101, 41))
        self.ram_lo.setStyleSheet("font-size: 30px;")
        self.ram_lo.setTextFormat(QtCore.Qt.AutoText)
        self.ram_lo.setScaledContents(False)
        self.ram_lo.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_lo.setObjectName("ram_lo")
        self.data_bus_address = QtWidgets.QLabel(self.background_image)
        self.data_bus_address.setGeometry(QtCore.QRect(500, 630, 101, 41))
        self.data_bus_address.setStyleSheet("font-size: 30px;")
        self.data_bus_address.setTextFormat(QtCore.Qt.AutoText)
        self.data_bus_address.setScaledContents(False)
        self.data_bus_address.setAlignment(QtCore.Qt.AlignCenter)
        self.data_bus_address.setObjectName("data_bus_address")
        self.prg_counter = QtWidgets.QLabel(self.background_image)
        self.prg_counter.setGeometry(QtCore.QRect(610, 210, 111, 41))
        self.prg_counter.setStyleSheet("font-size: 30px;")
        self.prg_counter.setTextFormat(QtCore.Qt.AutoText)
        self.prg_counter.setScaledContents(False)
        self.prg_counter.setAlignment(QtCore.Qt.AlignCenter)
        self.prg_counter.setObjectName("prg_counter")
        self.ins_address = QtWidgets.QLabel(self.background_image)
        self.ins_address.setGeometry(QtCore.QRect(460, 210, 91, 51))
        self.ins_address.setStyleSheet("font-size: 30px;\n"
                                       "color:blue;")
        self.ins_address.setTextFormat(QtCore.Qt.AutoText)
        self.ins_address.setScaledContents(False)
        self.ins_address.setAlignment(QtCore.Qt.AlignCenter)
        self.ins_address.setObjectName("ins_address")
        self.ram_hi = QtWidgets.QLabel(self.background_image)
        self.ram_hi.setGeometry(QtCore.QRect(120, 490, 101, 41))
        self.ram_hi.setStyleSheet("font-size: 30px;")
        self.ram_hi.setTextFormat(QtCore.Qt.AutoText)
        self.ram_hi.setScaledContents(False)
        self.ram_hi.setAlignment(QtCore.Qt.AlignCenter)
        self.ram_hi.setObjectName("ram_hi")
        self.ins_cmd = QtWidgets.QLabel(self.background_image)
        self.ins_cmd.setGeometry(QtCore.QRect(410, 210, 101, 51))
        self.ins_cmd.setStyleSheet("font-size: 30px;\n"
                                   "color:red;\n"
                                   "")
        self.ins_cmd.setTextFormat(QtCore.Qt.AutoText)
        self.ins_cmd.setScaledContents(False)
        self.ins_cmd.setAlignment(QtCore.Qt.AlignCenter)
        self.ins_cmd.setObjectName("ins_cmd")
        self.data_bus_cmd = QtWidgets.QLabel(self.background_image)
        self.data_bus_cmd.setGeometry(QtCore.QRect(440, 620, 101, 61))
        self.data_bus_cmd.setStyleSheet("font-size: 30px;")
        self.data_bus_cmd.setTextFormat(QtCore.Qt.AutoText)
        self.data_bus_cmd.setScaledContents(False)
        self.data_bus_cmd.setAlignment(QtCore.Qt.AlignCenter)
        self.data_bus_cmd.setObjectName("data_bus_cmd")
        self.data_bus_setter = QtWidgets.QTextEdit(self.background_image)
        self.data_bus_setter.setGeometry(QtCore.QRect(40, 630, 71, 31))
        self.data_bus_setter.setStyleSheet("font-size: 20px;")
        self.data_bus_setter.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_bus_setter.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.data_bus_setter.setObjectName("data_bus_setter")
        self.data_bus_set = QtWidgets.QPushButton(self.background_image)
        self.data_bus_set.setGeometry(QtCore.QRect(110, 610, 21, 71))
        self.data_bus_set.setText("")
        self.data_bus_set.setObjectName("data_bus_set")
        self.db_to_ram = QtWidgets.QPushButton(self.background_image)
        self.db_to_ram.setGeometry(QtCore.QRect(130, 580, 75, 23))
        self.db_to_ram.setObjectName("db_to_ram")
        self.ram_to_db = QtWidgets.QPushButton(self.background_image)
        self.ram_to_db.setGeometry(QtCore.QRect(210, 580, 75, 23))
        self.ram_to_db.setObjectName("ram_to_db")
        self.db_to_ins = QtWidgets.QPushButton(self.background_image)
        self.db_to_ins.setGeometry(QtCore.QRect(350, 410, 75, 23))
        self.db_to_ins.setObjectName("db_to_ins")
        self.ins_to_mc = QtWidgets.QPushButton(self.background_image)
        self.ins_to_mc.setGeometry(QtCore.QRect(420, 310, 75, 23))
        self.ins_to_mc.setObjectName("ins_to_mc")
        self.pc_increment_if_0 = QtWidgets.QPushButton(self.background_image)
        self.pc_increment_if_0.setGeometry(QtCore.QRect(630, 290, 75, 23))
        self.pc_increment_if_0.setObjectName("pc_increment_if_0")
        self.pc_increment = QtWidgets.QPushButton(self.background_image)
        self.pc_increment.setGeometry(QtCore.QRect(630, 320, 75, 23))
        self.pc_increment.setObjectName("pc_increment")
        self.mc_reset = QtWidgets.QPushButton(self.background_image)
        self.mc_reset.setGeometry(QtCore.QRect(630, 530, 75, 23))
        self.mc_reset.setObjectName("mc_reset")
        self.acc_hi = QtWidgets.QLabel(self.background_image)
        self.acc_hi.setGeometry(QtCore.QRect(810, 310, 101, 41))
        self.acc_hi.setStyleSheet("font-size: 30px;")
        self.acc_hi.setTextFormat(QtCore.Qt.AutoText)
        self.acc_hi.setScaledContents(False)
        self.acc_hi.setAlignment(QtCore.Qt.AlignCenter)
        self.acc_hi.setObjectName("acc_hi")
        self.mc_lo = QtWidgets.QLabel(self.background_image)
        self.mc_lo.setGeometry(QtCore.QRect(490, 355, 101, 41))
        self.mc_lo.setStyleSheet("font-size: 30px;")
        self.mc_lo.setTextFormat(QtCore.Qt.AutoText)
        self.mc_lo.setScaledContents(False)
        self.mc_lo.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_lo.setObjectName("mc_lo")
        self.mc_hi = QtWidgets.QLabel(self.background_image)
        self.mc_hi.setGeometry(QtCore.QRect(410, 355, 101, 41))
        self.mc_hi.setStyleSheet("font-size: 30px;")
        self.mc_hi.setTextFormat(QtCore.Qt.AutoText)
        self.mc_hi.setScaledContents(False)
        self.mc_hi.setAlignment(QtCore.Qt.AlignCenter)
        self.mc_hi.setObjectName("mc_hi")
        self.acc_lo = QtWidgets.QLabel(self.background_image)
        self.acc_lo.setGeometry(QtCore.QRect(860, 310, 101, 41))
        self.acc_lo.setStyleSheet("font-size: 30px;")
        self.acc_lo.setTextFormat(QtCore.Qt.AutoText)
        self.acc_lo.setScaledContents(False)
        self.acc_lo.setAlignment(QtCore.Qt.AlignCenter)
        self.acc_lo.setObjectName("acc_lo")
        self.ins_to_pc = QtWidgets.QPushButton(self.background_image)
        self.ins_to_pc.setGeometry(QtCore.QRect(550, 210, 75, 23))
        self.ins_to_pc.setObjectName("ins_to_pc")
        self.pc_to_ab = QtWidgets.QPushButton(self.background_image)
        self.pc_to_ab.setGeometry(QtCore.QRect(630, 130, 75, 23))
        self.pc_to_ab.setObjectName("pc_to_ab")
        self.ins_to_ab = QtWidgets.QPushButton(self.background_image)
        self.ins_to_ab.setGeometry(QtCore.QRect(470, 130, 75, 23))
        self.ins_to_ab.setObjectName("ins_to_ab")
        self.acc_reset = QtWidgets.QPushButton(self.background_image)
        self.acc_reset.setGeometry(QtCore.QRect(850, 62, 75, 41))
        self.acc_reset.setObjectName("acc_reset")
        self.acc_inc = QtWidgets.QPushButton(self.background_image)
        self.acc_inc.setGeometry(QtCore.QRect(850, 112, 75, 31))
        self.acc_inc.setObjectName("acc_inc")
        self.acc_dec = QtWidgets.QPushButton(self.background_image)
        self.acc_dec.setGeometry(QtCore.QRect(850, 152, 75, 31))
        self.acc_dec.setObjectName("acc_dec")
        self.add_to_acc = QtWidgets.QPushButton(self.background_image)
        self.add_to_acc.setGeometry(QtCore.QRect(750, 410, 75, 23))
        self.add_to_acc.setObjectName("add_to_acc")
        self.sub_to_acc = QtWidgets.QPushButton(self.background_image)
        self.sub_to_acc.setGeometry(QtCore.QRect(750, 450, 75, 23))
        self.sub_to_acc.setObjectName("sub_to_acc")
        self.db_to_acc = QtWidgets.QPushButton(self.background_image)
        self.db_to_acc.setGeometry(QtCore.QRect(750, 490, 75, 23))
        self.db_to_acc.setObjectName("db_to_acc")
        self.acc_to_db = QtWidgets.QPushButton(self.background_image)
        self.acc_to_db.setGeometry(QtCore.QRect(860, 490, 75, 23))
        self.acc_to_db.setObjectName("acc_to_db")
        self.mc_table = QtWidgets.QTableWidget(self.background_image)
        self.mc_table.setGeometry(QtCore.QRect(440, 400, 141, 171))
        self.mc_table.setLineWidth(1)
        self.mc_table.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.mc_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.mc_table.setDragEnabled(False)
        self.mc_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.mc_table.setShowGrid(True)
        self.mc_table.setObjectName("mc_table")

        self.stop_bt = QtWidgets.QPushButton(self.background_image)
        self.stop_bt.setGeometry(QtCore.QRect(630, 590, 75, 23))
        self.stop_bt.setObjectName("stop_bt")

        self.ram_info_change = QtWidgets.QTableWidget(self.background_image)
        self.ram_info_change.setGeometry(QtCore.QRect(90, 150, 231, 201))
        self.ram_info_change.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ram_info_change.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ram_info_change.setEditTriggers(QtWidgets.QAbstractItemView.SelectedClicked)
        self.ram_info_change.setObjectName("ram_info_change")

        self.ram_viewer = QtWidgets.QTableWidget(self.background_image)
        self.ram_viewer.setGeometry(QtCore.QRect(90, 360, 231, 131))
        self.ram_viewer.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.ram_viewer.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ram_viewer.setAutoScrollMargin(16)
        self.ram_viewer.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ram_viewer.setObjectName("ram_viewer")
        self.hide_cu = QtWidgets.QFrame(self.background_image)
        self.hide_cu.setGeometry(QtCore.QRect(350, 90, 371, 531))
        self.hide_cu.setStyleSheet("background-color: rgb(191, 191, 191);\n"
                                   "border-width:2px;\n"
                                   "border-style:solid;")
        self.hide_cu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.hide_cu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.hide_cu.setObjectName("hide_cu")
        self.color_change_if_zero = QtWidgets.QFrame(self.background_image)
        self.color_change_if_zero.setGeometry(QtCore.QRect(770, 287, 36, 29))
        self.color_change_if_zero.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                                "border-width:1px;\n"
                                                "border-style:solid;\n"
                                                "border-radius: 4px;")
        self.color_change_if_zero.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.color_change_if_zero.setFrameShadow(QtWidgets.QFrame.Raised)
        self.color_change_if_zero.setObjectName("color_change_if_zero")
        self.ram_address_set.raise_()
        self.ram_address_setter.raise_()
        self.ram_position.raise_()
        self.address_bus.raise_()
        self.ram_lo.raise_()
        self.data_bus_address.raise_()
        self.prg_counter.raise_()
        self.ins_address.raise_()
        self.ram_hi.raise_()
        self.ins_cmd.raise_()
        self.data_bus_cmd.raise_()
        self.data_bus_setter.raise_()
        self.data_bus_set.raise_()
        self.db_to_ram.raise_()
        self.ram_to_db.raise_()
        self.db_to_ins.raise_()
        self.ins_to_mc.raise_()
        self.pc_increment_if_0.raise_()
        self.pc_increment.raise_()
        self.mc_reset.raise_()
        self.acc_hi.raise_()
        self.acc_lo.raise_()
        self.ins_to_pc.raise_()
        self.pc_to_ab.raise_()
        self.ins_to_ab.raise_()
        self.acc_reset.raise_()
        self.acc_inc.raise_()
        self.acc_dec.raise_()
        self.add_to_acc.raise_()
        self.sub_to_acc.raise_()
        self.db_to_acc.raise_()
        self.acc_to_db.raise_()
        self.mc_table.raise_()
        self.ram_info_change.raise_()
        self.ram_viewer.raise_()
        self.mc_hi.raise_()
        self.mc_lo.raise_()
        self.color_change_if_zero.raise_()
        self.stop_bt.raise_()
        self.hide_cu.raise_()
        self.cat_img.raise_()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1011, 70))
        self.frame.setStyleSheet("background-color: rgb(229, 229, 229);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.new_ram = QtWidgets.QPushButton(self.frame)
        self.new_ram.setGeometry(QtCore.QRect(20, 15, 41, 41))
        self.new_ram.setStyleSheet("image: url(sprites/new_macro.png);")
        self.new_ram.setText("")
        self.new_ram.setObjectName("new_ram")
        self.open_ram = QtWidgets.QPushButton(self.frame)
        self.open_ram.setGeometry(QtCore.QRect(60, 15, 41, 41))
        self.open_ram.setStyleSheet("image: url(sprites/open_ram.png);")
        self.open_ram.setText("")
        self.open_ram.setObjectName("open_ram")
        self.save_ram = QtWidgets.QPushButton(self.frame)
        self.save_ram.setGeometry(QtCore.QRect(100, 15, 41, 41))
        self.save_ram.setStyleSheet("image: url(sprites/save_ram.png);")
        self.save_ram.setText("")
        self.save_ram.setObjectName("save_ram")
        self.next_step = QtWidgets.QPushButton(self.frame)
        self.next_step.setGeometry(QtCore.QRect(180, 15, 41, 41))
        self.next_step.setStyleSheet("image: url(sprites/macro_step.png);")
        self.next_step.setText("")
        self.next_step.setObjectName("next_step")
        self.run_macro_code = QtWidgets.QPushButton(self.frame)
        self.run_macro_code.setGeometry(QtCore.QRect(220, 15, 41, 41))
        self.run_macro_code.setStyleSheet("image: url(sprites/macro_run.png);")
        self.run_macro_code.setText("")
        self.run_macro_code.setObjectName("run_macro_code")
        self.reset_program = QtWidgets.QPushButton(self.frame)
        self.reset_program.setGeometry(QtCore.QRect(260, 15, 41, 41))
        self.reset_program.setStyleSheet("image: url(sprites/reset.png);")
        self.reset_program.setText("")
        self.reset_program.setObjectName("reset_program")
        self.show_control = QtWidgets.QPushButton(self.frame)
        self.show_control.setGeometry(QtCore.QRect(370, 5, 111, 61))
        self.show_control.setStyleSheet("image: url(sprites/show_command.png);")
        self.show_control.setText("")
        self.show_control.setCheckable(True)
        self.show_control.setChecked(False)
        self.show_control.setObjectName("show_control")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(390, 20, 16, 17))
        self.checkBox.setText("")
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setEnabled(False)
        MainWindow.setCentralWidget(self.centralwidget)
        iconMainWindow = QIcon("sprites/guido_logo.png")
        iconDialog = QIcon("sprites/line_to_ram.png")
        MainWindow.setWindowIcon(iconMainWindow)
        dialog.ram_change_menu.setWindowIcon(iconDialog)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Johnny Computer"))
        self.ram_address_setter.setPlaceholderText(_translate("MainWindow", "000"))
        self.ram_position.setText(_translate("MainWindow", "000"))
        self.address_bus.setText(_translate("MainWindow", "000"))
        self.ram_lo.setText(_translate("MainWindow", "000"))
        self.data_bus_address.setText(_translate("MainWindow", "000"))
        self.prg_counter.setText(_translate("MainWindow", "000"))
        self.ins_address.setText(_translate("MainWindow", "000"))
        self.ram_hi.setText(_translate("MainWindow", "00"))
        self.ins_cmd.setText(_translate("MainWindow", "00"))
        self.data_bus_cmd.setText(_translate("MainWindow", "00"))
        self.data_bus_setter.setPlaceholderText(_translate("MainWindow", "00000"))
        self.db_to_ram.setText(_translate("MainWindow", "db->ram"))
        self.ram_to_db.setText(_translate("MainWindow", "ram->db"))
        self.db_to_ins.setText(_translate("MainWindow", "db->ins"))
        self.ins_to_mc.setText(_translate("MainWindow", "ins->mc"))
        self.stop_bt.setText(_translate("MainWindow", "stop"))
        self.pc_increment_if_0.setText(_translate("MainWindow", "=0:pc++"))
        self.pc_increment.setText(_translate("MainWindow", "pc++"))
        self.mc_reset.setText(_translate("MainWindow", "mc:=0"))
        self.acc_hi.setText(_translate("MainWindow", "00"))
        self.acc_lo.setText(_translate("MainWindow", "000"))
        self.ins_to_pc.setText(_translate("MainWindow", "ins->pc"))
        self.pc_to_ab.setText(_translate("MainWindow", "pc->ab"))
        self.ins_to_ab.setText(_translate("MainWindow", "ins->ab"))
        self.acc_reset.setText(_translate("MainWindow", "acc:=0"))
        self.acc_inc.setText(_translate("MainWindow", "acc++"))
        self.acc_dec.setText(_translate("MainWindow", "acc--"))
        self.add_to_acc.setText(_translate("MainWindow", "plus"))
        self.sub_to_acc.setText(_translate("MainWindow", "minus"))
        self.db_to_acc.setText(_translate("MainWindow", "db->acc"))
        self.acc_to_db.setText(_translate("MainWindow", "acc->db"))
        self.mc_hi.setText(_translate("MainWindow", "00"))
        self.mc_lo.setText(_translate("MainWindow", "0"))

    def init(self):
        self.ram_position.setText("000")
        self.address_bus.setText("000")
        self.prg_counter.setText("000")
        self.ins_address.setText("000")
        self.ram_address_setter.setText("")
        self.ram_info_change.setCurrentCell(0, 0)
        self.frame.setEnabled(False)
        self.background_image.setEnabled(False)
        dialog.ram_change_menu.closeEvent = lambda event: MainWindow.setEnabled(True)

    def resetareProgram(self):
        self.ram_position.setText("000")
        self.address_bus.setText("000")
        self.prg_counter.setText("000")
        self.ins_address.setText("000")
        self.data_bus_address.setText("000")
        self.data_bus_cmd.setText("00")
        self.accReset()
        self.mcReset()
        self.ram_address_setter.setText("")
        self.ram_info_change.setCurrentCell(0, 0)
        self.prg_counter.setText("000")
        self.ins_cmd.setText("00")

    def openDialog(self):
        value = int(self.ram_info_change.item(ramTable.row, 1).text())
        if value >= 0 and value <= 10:
            dialog.ui.hi_selector.setCurrentIndex(value)
        else:
            dialog.ui.hi_selector.setCurrentIndex(0)
        dialog.ui.hi_text_edit.setText(self.ram_info_change.item(ramTable.row, 1).text())
        dialog.ui.lo_text_edit.setText(self.ram_info_change.item(ramTable.row, 2).text())
        dialog.ui.adress_label.setText(self.ram_info_change.item(ramTable.row, 0).text() + ":")
        dialog.ram_change_menu.show()

    def showControl(self):
        if self.show_control.isChecked() == True:
            self.checkBox.setChecked(True)
            self.hide_cu.hide()
        else:
            self.checkBox.setChecked(False)
            self.hide_cu.show()

    def ramAddressSet(self):
        if self.ram_address_setter.toPlainText() != "":
            value = int(self.ram_address_setter.toPlainText())
        else:
            value = 0
        if value >= 0 and value <= 9:
            self.address_bus.setText("00" + str(value))
            self.ram_position.setText(self.address_bus.text())
        if value > 9 and value <= 99:
            self.address_bus.setText("0" + str(value))
            self.ram_position.setText(self.address_bus.text())
        if value > 99 and value <= 999:
            self.address_bus.setText(str(value))
            self.ram_position.setText(self.address_bus.text())
        ram_view.ramViewMove(value)
        self.setRamLabel()

    def pcToAb(self):
        self.address_bus.setText(self.prg_counter.text())
        self.ram_position.setText(self.address_bus.text())
        ram_view.ramViewMove(int(self.ram_position.text()))

    def insToAb(self):
        self.address_bus.setText(self.ins_address.text())
        self.ram_position.setText(self.address_bus.text())
        ram_view.ramViewMove(int(self.ram_position.text()))

    def insToPc(self):
        self.prg_counter.setText(self.ins_address.text())

    def dbToIns(self):
        lo = self.data_bus_address.text()
        hi = self.data_bus_cmd.text()
        self.ins_address.setText(lo)
        self.ins_cmd.setText(hi)

    def insToMc(self):
        hi = self.data_bus_cmd.text()
        self.mc_hi.setText(hi)
        micro_cod.updateCMD()

    def mcReset(self):
        self.mc_hi.setText("00")
        self.mc_lo.setText("0")
        self.mc_table.setCurrentCell(0, 0)

    def ramToDb(self):
        self.data_bus_address.setText(self.ram_lo.text())
        self.data_bus_cmd.setText(self.ram_hi.text())

    def dbToRam(self):
        linie = self.ram_viewer.currentRow()
        hi = self.data_bus_cmd.text()
        lo = self.data_bus_address.text()
        ramTable.setInfo(hi, lo, linie)

    def ripCat(self):
        self.cat_img.hide()
        self.frame.setEnabled(True)
        self.background_image.setEnabled(True)

    def dbToAcc(self):
        lo = self.data_bus_address.text()
        hi = self.data_bus_cmd.text()
        self.acc_lo.setText(lo)
        self.acc_hi.setText(hi)

    def accToDb(self):
        lo = self.acc_lo.text()
        hi = self.acc_hi.text()
        self.data_bus_address.setText(lo)
        self.data_bus_cmd.setText(hi)

    def resetRamLine(self):
        linie = self.ram_viewer.currentRow()
        self.ram_info_change.setItem(linie, 1, QTableWidgetItem("00"))
        self.ram_info_change.setItem(linie, 2, QTableWidgetItem("000"))
        self.ram_info_change.setItem(linie, 3, QTableWidgetItem(""))
        self.ram_info_change.setItem(linie, 4, QTableWidgetItem(""))

    def setRamLabel(self):
        linie = self.ram_viewer.currentRow()
        hi = self.ram_viewer.item(linie, 1).text()
        lo = self.ram_viewer.item(linie, 2).text()
        self.ram_hi.setText(hi)
        self.ram_lo.setText(lo)

    def setDataBus(self):
        text = self.data_bus_setter.toPlainText().zfill(5)
        self.data_bus_setter.setText(text)
        hi = text[:2]
        lo = text[2:5]
        self.data_bus_address.setText(lo)
        self.data_bus_cmd.setText(hi)

    def closeDialog(self):
        dialog.close()

    def accDiff(self):
        lo = int(self.data_bus_address.text())
        hi = int(self.data_bus_cmd.text())
        diff_lo = int(self.acc_lo.text()) - lo
        diff_hi = int(self.acc_hi.text()) - hi
        if diff_lo < 0 and diff_hi > 0:
            diff_hi -= 1
            diff_lo += 1000
        elif diff_lo < 0 and diff_hi == 0:
            diff_lo = 0
        self.acc_lo.setText(str(diff_lo).zfill(3))
        self.acc_hi.setText(str(diff_hi).zfill(2))
        self.checkIfAccZero()

    def accInc(self):
        lo = int(self.acc_lo.text()) + 1
        hi = int(self.acc_hi.text())
        if int(lo / 1000) == 1:
            hi += 1
            lo -= 1000
        self.acc_lo.setText(str(lo).zfill(3))
        self.acc_hi.setText(str(hi).zfill(2))
        self.checkIfAccZero()

    def checkIfAccZero(self):
        lo = int(self.acc_lo.text())
        hi = int(self.acc_hi.text())
        if hi + lo == 0:
            self.color_change_if_zero.setStyleSheet("background-color: rgb(255, 255, 0);\n"
                                                    "border-width:1px;\n"
                                                    "border-style:solid;\n"
                                                    "border-radius: 4px;")
            return True
        else:
            self.color_change_if_zero.setStyleSheet("background-color: rgb(0,0, 0);\n"
                                                    "border-width:1px;\n"
                                                    "border-style:solid;\n"
                                                    "border-radius: 4px;")
            return False

    def accDec(self):
        lo = int(self.acc_lo.text()) - 1
        hi = int(self.acc_hi.text())
        if lo < 0 and hi > 0:
            hi -= 1
            lo += 1000
        elif lo < 0 and hi == 0:
            lo = 0
        self.acc_lo.setText(str(lo).zfill(3))
        self.acc_hi.setText(str(hi).zfill(2))
        self.checkIfAccZero()

    def accPlus(self):
        lo = int(self.data_bus_address.text())
        hi = int(self.data_bus_cmd.text())
        suma_lo = int(self.acc_lo.text()) + lo
        suma_hi = int(self.acc_hi.text()) + hi
        if int(suma_lo / 1000) == 1:
            suma_hi += 1
            suma_lo -= 1000
        self.acc_lo.setText(str(suma_lo).zfill(3))
        self.acc_hi.setText(str(suma_hi).zfill(2))
        self.checkIfAccZero()

    def pcIncIf0(self):
        if self.checkIfAccZero():
            self.pcInc()

    def pcInc(self):
        counter = int(self.prg_counter.text())
        counter += 1
        self.prg_counter.setText(str(counter).zfill(3))

    def insToPc(self):
        lo = self.ins_address.text()
        self.prg_counter.setText(lo)

    def accReset(self):
        self.acc_lo.setText("000")
        self.acc_hi.setText("00")
        self.checkIfAccZero()

    def stop(self):
        msg = QMessageBox()

        msg.setText("Programul a fost rulat    ")
        msg.setWindowTitle("Finish")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def loadRam(self):
        of = QFileDialog.getOpenFileName(MainWindow, 'Open RAM File', "./", "RAM File (*.ram)")
        ramTable.ramReset()
        row = 0
        if (of[0] != ""):
            with open(of[0]) as fp:
                for line in fp:
                    temp = line.strip()
                    if len(temp) > 5 or (not temp.isdigit()):
                        msg = QMessageBox()
                        msg.setText("Linia " + str(row + 1) + " este invalida.")
                        msg.setWindowTitle("Error")
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.exec_()
                        break
                    if row == self.ram_info_change.rowCount():
                        break
                    temp = temp.zfill(5)
                    ramTable.setInfo(temp[:2], temp[2:5], row)
                    row += 1

    def saveRam(self):
        of = QFileDialog.getSaveFileName(MainWindow, 'Save RAM File', "./", "RAM File (*.ram)")
        if (of[0] != ""):
            with open(of[0], "a") as fp:
                for i in range(self.ram_info_change.rowCount()):
                    fp.write(self.ram_info_change.item(i, 1).text() + self.ram_info_change.item(i, 2).text() + '\n')

    def nextStep(self):
        micro_cod.ok = 1
        micro_cod.runCode()

        selected = self.prg_counter.text()
        self.ram_info_change.setCurrentCell(int(selected), 0)

    def buttonEventsInit(self):
        self.ram_address_set.clicked.connect(self.ramAddressSet)
        self.show_control.clicked.connect(self.showControl)
        self.pc_to_ab.clicked.connect(self.pcToAb)
        self.ins_to_ab.clicked.connect(self.insToAb)
        self.ins_to_pc.clicked.connect(self.insToPc)
        self.cat_img.mouseReleaseEvent = lambda event: self.ripCat()
        self.reset_program.clicked.connect(self.resetareProgram)
        dialog.ui.push_ram_info.clicked.connect(ramTable.pushInfo)
        dialog.ui.cancel_button.clicked.connect(self.closeDialog)
        dialog.ui.hi_lo_reset.clicked.connect(ramTable.resetHiLo)
        self.ram_to_db.clicked.connect(self.ramToDb)
        self.data_bus_set.clicked.connect(self.setDataBus)
        self.db_to_ram.clicked.connect(self.dbToRam)
        self.add_to_acc.clicked.connect(self.accPlus)
        self.sub_to_acc.clicked.connect(self.accDiff)
        self.db_to_acc.clicked.connect(self.dbToAcc)
        self.acc_to_db.clicked.connect(self.accToDb)
        self.acc_inc.clicked.connect(self.accInc)
        self.acc_dec.clicked.connect(self.accDec)
        self.acc_reset.clicked.connect(self.accReset)
        self.mc_reset.clicked.connect(self.mcReset)
        self.db_to_ins.clicked.connect(self.dbToIns)
        self.ins_to_mc.clicked.connect(self.insToMc)
        self.ins_to_pc.clicked.connect(self.insToPc)
        self.pc_increment_if_0.clicked.connect(self.pcIncIf0)
        self.pc_increment.clicked.connect(self.pcInc)
        self.new_ram.clicked.connect(ramTable.ramReset)
        self.next_step.clicked.connect(self.nextStep)
        self.run_macro_code.clicked.connect(micro_cod.runUntilStop)
        self.open_ram.clicked.connect(self.loadRam)
        self.save_ram.clicked.connect(self.saveRam)


class MicroCode:
    count = 0
    ok = 1
    dictionar = {"000": "000:fetch",
                 "010": "010:TAKE",
                 "020": "020:ADD",
                 "030": "030:SUB",
                 "040": "040:SAVE",
                 "050": "050:JMP",
                 "060": "060:TST",
                 "070": "070:INC",
                 "080": "080:DEC",
                 "090": "090:NULL",
                 "100": "100:HLT"}
    fetch = ["pc->ab", "ram->db", "db->ins", "ins->mc"]
    TAKE = ["acc:=0", "ins->ab", "ram->db", "plus", "pc++", "mc:=0"]
    ADD = ["ins->ab", "ram->db", "plus", "pc++", "mc:=0"]
    SUB = ["ins->ab", "ram->db", "minus", "pc++", "mc:=0"]
    SAVE = ["ins->ab", "acc->db", "db->ram", "pc++", "mc:=0"]
    JMP = ["ins->pc", "mc:=0"]
    TST = ["ins->ab", "ram->db", "db->acc", "=0:pc++", "pc++", "mc:=0"]
    INC = ["acc:=0", "ins->ab", "ram->db", "plus", "acc++", "acc->db", "db->ram", "pc++", "mc:=0"]
    DEC = ["acc:=0", "ins->ab", "ram->db", "plus", "acc--", "acc->db", "db->ram", "pc++", "mc:=0"]
    NULL = ["ins->ab", "acc:=0", "acc->db", "db->ram", "pc++", "mc:=0"]
    HLT = ["stop", "mc:=0"]

    def microCodeInit(self):
        ui.mc_table.setRowCount(102)
        ui.mc_table.setColumnCount(2)
        columns = ['', '']
        ui.mc_table.verticalHeader().hide()
        ui.mc_table.setHorizontalHeaderLabels(columns)
        ui.mc_table.setColumnWidth(0, 65)
        ui.mc_table.setColumnWidth(1, 65)
        ui.mc_table.setStyleSheet("selection-background-color: #FA057F;\n"
                                  "font-size:12px;")
        newfont = QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)

        for i in range(ui.mc_table.rowCount()):
            text = ""
            if str(self.count).zfill(3) in self.dictionar:
                ui.mc_table.setItem(i, 0, QTableWidgetItem(self.dictionar[str(self.count).zfill(3)]))
            else:
                ui.mc_table.setItem(i, 0, QTableWidgetItem(str(self.count).zfill(3)))
            self.count += 1

        ui.mc_table.setSelectionBehavior(QAbstractItemView.SelectRows)

        for i in range(len(self.fetch)):
            ui.mc_table.setItem(i, 1, QTableWidgetItem(self.fetch[i]))
        for i in range(len(self.TAKE)):
            ui.mc_table.setItem(10 + i, 1, QTableWidgetItem(self.TAKE[i]))

        for i in range(len(self.ADD)):
            ui.mc_table.setItem(20 + i, 1, QTableWidgetItem(self.ADD[i]))
        for i in range(len(self.SUB)):
            ui.mc_table.setItem(30 + i, 1, QTableWidgetItem(self.SUB[i]))
        for i in range(len(self.SAVE)):
            ui.mc_table.setItem(40 + i, 1, QTableWidgetItem(self.SAVE[i]))
        for i in range(len(self.JMP)):
            ui.mc_table.setItem(50 + i, 1, QTableWidgetItem(self.JMP[i]))
        for i in range(len(self.TST)):
            ui.mc_table.setItem(60 + i, 1, QTableWidgetItem(self.TST[i]))
        for i in range(len(self.INC)):
            ui.mc_table.setItem(70 + i, 1, QTableWidgetItem(self.INC[i]))
        for i in range(len(self.DEC)):
            ui.mc_table.setItem(80 + i, 1, QTableWidgetItem(self.DEC[i]))
        for i in range(len(self.NULL)):
            ui.mc_table.setItem(90 + i, 1, QTableWidgetItem(self.NULL[i]))
        for i in range(len(self.HLT)):
            ui.mc_table.setItem(100 + i, 1, QTableWidgetItem(self.HLT[i]))

        for i in range(100):
            if ui.mc_table.item(i, 1) == None:
                ui.mc_table.setItem(i, 1, QTableWidgetItem("---"))
        ui.mc_table.setCurrentCell(0, 0)

    def runUntilStop(self):
        hi = int(ui.ins_cmd.text()) * 10
        while hi < 100:
            self.ok = 1
            self.runCode()
            hi = int(ui.ins_cmd.text()) * 10
            if hi == 0:
                break

    def updateCMD(self):
        hi = int(ui.mc_hi.text()) * 10
        ui.mc_table.setCurrentCell(hi, 0)

    def runCode(self):
        hi = int(ui.mc_hi.text()) * 10
        if hi == 0:
            ui.pcToAb()
            ui.ramToDb()
            ui.dbToIns()
            ui.insToMc()
            if self.ok == 1:
                self.ok = 0
                self.runCode()

        elif hi == 10:
            ui.accReset()
            ui.insToAb()
            ui.ramToDb()
            ui.accPlus()
            ui.pcInc()
            ui.mcReset()
        elif hi == 20:
            ui.insToAb()
            ui.ramToDb()
            ui.accPlus()
            ui.pcInc()
            ui.mcReset()
        elif hi == 30:
            ui.insToAb()
            ui.ramToDb()
            ui.accDiff()
            ui.pcInc()
            ui.mcReset()
        elif hi == 40:
            ui.insToAb()
            ui.accToDb()
            ui.dbToRam()
            ui.pcInc()
            ui.mcReset()
        elif hi == 50:
            ui.insToPc()
            ui.mcReset()
        elif hi == 60:
            ui.insToAb()
            ui.ramToDb()
            ui.dbToAcc()
            ui.pcIncIf0()
            ui.pcInc()
            ui.mcReset()
        elif hi == 70:
            ui.accReset()
            ui.insToAb()
            ui.ramToDb()
            ui.accPlus()
            ui.accInc()
            ui.accToDb()
            ui.dbToRam()
            ui.pcInc()
            ui.mcReset()
        elif hi == 80:
            ui.accReset()
            ui.insToAb()
            ui.ramToDb()
            ui.accPlus()
            ui.accDec()
            ui.accToDb()
            ui.dbToRam()
            ui.pcInc()
            ui.mcReset()
        elif hi == 90:
            ui.insToAb()
            ui.accReset()
            ui.accToDb()
            ui.dbToRam()
            ui.pcInc()
            ui.mcReset()
        else:
            ui.stop()
            ui.mcReset()


class RamLine:
    dictionar = {"00": "",
                 "01": "TAKE",
                 "02": "ADD",
                 "03": "SUB",
                 "04": "SAVE",
                 "05": "JMP",
                 "06": "TST",
                 "07": "INC",
                 "08": "DEC",
                 "09": "NULL",
                 "10": "HLT"}

    def cell_was_clicked(self, row, column):
        self.row = row
        self.column = column
        MainWindow.setEnabled(False)
        ui.openDialog()

    def setInfo(self, hi, lo, linie):
        value_lo = int(lo)
        value_hi = int(hi)
        if value_lo >= 0 and value_lo <= 9:
            ui.ram_info_change.setItem(linie, 4, QTableWidgetItem("00" + str(value_lo)))
            ui.ram_info_change.setItem(linie, 2, QTableWidgetItem("00" + str(value_lo)))
        elif value_lo > 9 and value_lo <= 99:
            ui.ram_info_change.setItem(linie, 4, QTableWidgetItem("0" + str(value_lo)))
            ui.ram_info_change.setItem(linie, 2, QTableWidgetItem("0" + str(value_lo)))
        elif value_lo > 99 and value_lo <= 999:
            ui.ram_info_change.setItem(linie, 4, QTableWidgetItem(str(value_lo)))
            ui.ram_info_change.setItem(linie, 2, QTableWidgetItem(str(value_lo)))
        else:
            ui.ram_info_change.setItem(linie, 4, QTableWidgetItem(""))
            ui.ram_info_change.setItem(linie, 3, QTableWidgetItem(""))
        if value_hi == 0:
            ui.ram_info_change.setItem(linie, 1, QTableWidgetItem("00"))
            ui.ram_info_change.setItem(linie, 4, QTableWidgetItem(""))
            ui.ram_info_change.setItem(linie, 3, QTableWidgetItem(""))
        if value_hi >= 1 and value_hi <= 9:
            ui.ram_info_change.setItem(linie, 1, QTableWidgetItem("0" + str(value_hi)))
        elif value_hi > 9 and value_hi <= 99:
            ui.ram_info_change.setItem(linie, 1, QTableWidgetItem(str(value_hi)))
        if ui.ram_info_change.item(linie, 1).text() in self.dictionar:
            ui.ram_info_change.setItem(linie, 3,
                                       QTableWidgetItem(self.dictionar[ui.ram_info_change.item(linie, 1).text()]))
        if value_hi <= 0:
            ui.ram_info_change.setItem(linie, 4, QTableWidgetItem(""))
            ui.ram_info_change.setItem(linie, 3, QTableWidgetItem(""))
        ram_view.setRamViewInfo(linie)

    def pushInfo(self):
        lo = dialog.ui.lo_text_edit.text()
        hi = dialog.ui.hi_text_edit.text()
        self.setInfo(hi, lo, self.row)
        dialog.close()

    def resetHiLo(self):
        dialog.ui.hi_text_edit.setText("00")
        dialog.ui.lo_text_edit.setText("000")
        ui.ram_info_change.setItem(self.row, 1, QTableWidgetItem(str(dialog.ui.hi_text_edit.text())))
        ui.ram_info_change.setItem(self.row, 2, QTableWidgetItem(str(dialog.ui.lo_text_edit.text())))
        ui.ram_info_change.setItem(self.row, 4, QTableWidgetItem(""))
        ui.ram_info_change.setItem(self.row, 3, QTableWidgetItem(""))
        ram_view.setRamViewInfo(self.row)
        dialog.close()

    def ramInit(self):
        ui.ram_info_change.setRowCount(500)
        ui.ram_info_change.setColumnCount(5)
        columns = ['ADR', 'HI', 'LO', 'ASM', 'OPND']
        ui.ram_info_change.verticalHeader().hide()
        ui.ram_info_change.setHorizontalHeaderLabels(columns)
        ui.ram_info_change.setColumnWidth(0, 20)
        ui.ram_info_change.setColumnWidth(1, 20)
        ui.ram_info_change.setColumnWidth(2, 20)
        ui.ram_info_change.setColumnWidth(3, 45)
        ui.ram_info_change.setColumnWidth(4, 50)
        ui.ram_info_change.setStyleSheet("selection-background-color: #FA057F;")
        newfont = QtGui.QFont("Helvetica", 10, QtGui.QFont.Bold)
        for i in range(5):
            ui.ram_info_change.horizontalHeaderItem(i).setFont(newfont)
            ui.ram_info_change.horizontalHeaderItem(i)

        ui.ram_info_change.cellClicked.connect(self.cell_was_clicked)
        for i in range(ui.ram_info_change.rowCount()):
            ui.ram_info_change.setItem(i, 0, QTableWidgetItem(str(i).zfill(3)))
            ui.ram_info_change.setItem(i, 1, QTableWidgetItem("00"))
            ui.ram_info_change.setItem(i, 2, QTableWidgetItem("000"))
            # ui.ram_info_change.setItem(i, 3, QTableWidgetItem(""))
            # ui.ram_info_change.setItem(i, 4, QTableWidgetItem(""))
        ui.ram_info_change.setSelectionBehavior(QAbstractItemView.SelectRows)

    def ramReset(self):
        for i in range(ui.ram_info_change.rowCount()):
            ui.ram_info_change.setItem(i, 1, QTableWidgetItem("00"))
            ui.ram_info_change.setItem(i, 2, QTableWidgetItem("000"))
            ui.ram_info_change.setItem(i, 3, QTableWidgetItem(""))
            ui.ram_info_change.setItem(i, 4, QTableWidgetItem(""))
            ram_view.setRamViewInfo(i)


class RamView:
    def ramViewInit(self):
        ui.ram_viewer.setStyleSheet("selection-background-color: cyan;\n"
                                    "selection-color: black;")
        ui.ram_viewer.setRowCount(500)
        ui.ram_viewer.setColumnCount(5)
        ui.ram_viewer.verticalHeader().hide()
        ui.ram_viewer.setColumnWidth(0, 20)
        ui.ram_viewer.setColumnWidth(1, 20)
        ui.ram_viewer.setColumnWidth(2, 20)
        ui.ram_viewer.setColumnWidth(3, 45)
        ui.ram_viewer.setColumnWidth(4, 50)
        ui.ram_viewer.horizontalHeader().hide()
        for i in range(ui.ram_viewer.rowCount()):
            ui.ram_viewer.setItem(i, 0, QTableWidgetItem(str(i).zfill(3)))
            ui.ram_viewer.setItem(i, 1, QTableWidgetItem("00"))
            ui.ram_viewer.setItem(i, 2, QTableWidgetItem("000"))
        ui.ram_viewer.setSelectionBehavior(QAbstractItemView.SelectRows)
        ui.ram_viewer.setEnabled(False)
        ui.ram_viewer.setCurrentCell(0, 0)

    def ramViewMove(self, index):
        ui.ram_viewer.setCurrentCell(index, 0)
        hi = ui.ram_viewer.item(index, 1).text()
        lo = ui.ram_viewer.item(index, 2).text()
        ui.ram_hi.setText(hi)
        ui.ram_lo.setText(lo)

    def setRamViewInfo(self, row):
        ui.ram_viewer.setItem(row, 1, QTableWidgetItem(ui.ram_info_change.item(row, 1).text()))
        ui.ram_viewer.setItem(row, 2, QTableWidgetItem(ui.ram_info_change.item(row, 2).text()))
        ui.ram_viewer.setItem(row, 3, QTableWidgetItem(ui.ram_info_change.item(row, 3).text()))
        ui.ram_viewer.setItem(row, 4, QTableWidgetItem(ui.ram_info_change.item(row, 4).text()))
        ui.setRamLabel()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ramTable = RamLine()
    ram_view = RamView()
    micro_cod = MicroCode()
    dialog = Dialog_UI.Dialog()
    ui.setupUi(MainWindow)
    ui.buttonEventsInit()
    ramTable.ramInit()
    ram_view.ramViewInit()
    micro_cod.microCodeInit()
    ui.init()
    MainWindow.show()
    sys.exit(app.exec_())
