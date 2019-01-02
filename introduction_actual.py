# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'introducation.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(374, 465)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 374, 465))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setText("1.目录选择：\n选择地图默认的存档文件目录，即.../魔兽安装目录/TWRPG\n\n" +
                                 "2.全部刷新：\n从存档目录重新加载存档文件数据，在每次游戏save后应使用该项\n\n" +
                                 "3.全部导出：\n将表格中的存档数据导出到该程序所在目录的records.txt文件中\n\n" +
                                 "4.全部导入：\n从该程序所在目录的redocrds.txt文件中加载存档数据\n\n" +
                                 "注：全部导出和全部导入方便在不同地点上网时快速转移存档，如有人喜欢在家里和公司同时玩")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "使用说明"))
