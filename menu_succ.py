# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import configparser
import os
import os.path
import time as t

from PyQt5 import QtCore, QtGui, QtWidgets

import regex_controll


class Ui_form_base(QtWidgets.QWidget):
    chosen_path = ""

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
        self.button_choose_dict.clicked.connect(self.show_dialog)

        self.botton_refresh = QtWidgets.QPushButton(form_base)
        self.botton_refresh.setGeometry(QtCore.QRect(30, 75, 75, 23))
        self.botton_refresh.setObjectName("botton_refresh")
        self.botton_refresh.clicked.connect(self.show_refresh_data)

        self.table_data = QtWidgets.QTableView(form_base)
        self.table_data.setGeometry(QtCore.QRect(10, 130, 761, 331))
        self.table_data.setObjectName("table_data")
        self.model = QtGui.QStandardItemModel()
        self.table_data.horizontalHeader().setStretchLastSection(True)
        # self.table_data.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_data.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.table_data.setModel(self.model)
        self.re_init_headers()

        self.label_tips = QtWidgets.QLabel(form_base)
        self.label_tips.setGeometry(QtCore.QRect(120, 80, 551, 16))
        self.label_tips.setText("")
        self.label_tips.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tips.setStyleSheet("color:red")
        self.label_tips.setObjectName("label_tips")

        self.retranslateUi(form_base)
        QtCore.QMetaObject.connectSlotsByName(form_base)

        self.upload_setting_file()

    def upload_setting_file(self):
        if os.path.exists('setting.ini'):
            config = configparser.ConfigParser()
            config.read_file(open('setting.ini', encoding='utf-8'))
            existed_path = config.get('location', 'path')
            self.chosen_path = existed_path
            self.line_path.setText(existed_path)
            self.show_archive_info()
        else:
            pass

    def re_init_headers(self):
        self.model.setHorizontalHeaderLabels(['时间','文件名', '职业', '等级', '存档代码'])
        self.table_data.setColumnWidth(0, 140)
        self.table_data.setColumnWidth(1, 80)
        self.table_data.setColumnWidth(2, 60)
        self.table_data.setColumnWidth(3, 40)
        self.table_data.setColumnWidth(4, 400)

    def show_refresh_data(self):
        if regex_controll.check_valid_path(self.chosen_path):
            pass
        else:
            self.label_tips.setText("请先选择正确的存档目录!")
            return
        self.show_archive_info()

    def show_archive_info(self):
        try:
            files = os.listdir(self.chosen_path)
            self.model.clear()
            self.re_init_headers()
            for file in files:
                file_path = self.chosen_path + "/" + file
                f = open(file_path, "r", encoding='utf-8')
                mtime = os.stat(file_path).st_mtime
                file_modify_time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime(mtime))
                text = f.read()
                job = regex_controll.findJob(text)
                degree = regex_controll.findDegree(text)
                code = regex_controll.findCode(text)

                self.model.appendRow([QtGui.QStandardItem(file_modify_time),
                                      QtGui.QStandardItem(file),
                                      QtGui.QStandardItem(job),
                                      QtGui.QStandardItem(degree),
                                      QtGui.QStandardItem(code)])
                f.close()
        except Exception as err:
            print(err)

    def show_dialog(self):
        try:
            dict_path = QtWidgets.QFileDialog.getExistingDirectory(self, 'open file', '/')
            self.line_path.setText(dict_path)
            self.chosen_path = dict_path
            self.save_or_update_path()
        except Exception as err:
            print(err)

    def save_or_update_path(self):
        config = configparser.ConfigParser()
        config.add_section("location")
        config.set("location", "path", self.chosen_path)
        config.write(open('setting.ini', "w", encoding='utf-8'))

    def retranslateUi(self, form_base):
        _translate = QtCore.QCoreApplication.translate
        form_base.setWindowTitle(_translate("form_base", "世界ORPG存取档管理器v1.0 by 执着的小浮云"))
        form_base.setToolTip(_translate("form_base", "<html><head/><body><p><br/></p></body></html>"))
        self.label_path.setText(_translate("form_base", "存档目录"))
        self.button_choose_dict.setText(_translate("form_base", "目录选择"))
        self.botton_refresh.setText(_translate("form_base", "全部刷新"))
