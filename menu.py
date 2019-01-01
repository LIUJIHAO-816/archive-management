# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form_base(object):
    def setupUi(self, form_base):
        form_base.setObjectName("form_base")
        form_base.resize(781, 465)
        self.label_path = QtWidgets.QLabel(form_base)
        self.label_path.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")
        self.line_path = QtWidgets.QLineEdit(form_base)
        self.line_path.setGeometry(QtCore.QRect(90, 20, 511, 21))
        self.line_path.setObjectName("line_path")
        self.button_choose_dict = QtWidgets.QPushButton(form_base)
        self.button_choose_dict.setGeometry(QtCore.QRect(620, 20, 75, 23))
        self.button_choose_dict.setObjectName("button_choose_dict")
        self.botton_refresh = QtWidgets.QPushButton(form_base)
        self.botton_refresh.setGeometry(QtCore.QRect(30, 80, 75, 23))
        self.botton_refresh.setObjectName("botton_refresh")
        self.table_data = QtWidgets.QTableView(form_base)
        self.table_data.setGeometry(QtCore.QRect(10, 130, 761, 331))
        self.table_data.setObjectName("table_data")
        self.label_tips = QtWidgets.QLabel(form_base)
        self.label_tips.setGeometry(QtCore.QRect(120, 80, 551, 16))
        self.label_tips.setText("")
        self.label_tips.setObjectName("label_tips")

        self.retranslateUi(form_base)
        QtCore.QMetaObject.connectSlotsByName(form_base)

    def retranslateUi(self, form_base):
        _translate = QtCore.QCoreApplication.translate
        form_base.setWindowTitle(_translate("form_base", "世界ORPG存取档管理器v1.0 by 执着的小浮云"))
        form_base.setToolTip(_translate("form_base", "<html><head/><body><p><br/></p></body></html>"))
        self.label_path.setText(_translate("form_base", "存档目录"))
        self.button_choose_dict.setText(_translate("form_base", "目录选择"))
        self.botton_refresh.setText(_translate("form_base", "全部刷新"))

