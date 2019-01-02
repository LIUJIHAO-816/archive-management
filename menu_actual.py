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
import win32clipboard as winclb

from PyQt5 import QtCore, QtGui, QtWidgets

import introduction_actual as introduction
import regex_controll


class Ui_form_base(QtWidgets.QWidget):
    chosen_path = ""
    global intro

    def initUiRight(self):
        self.intro = QtWidgets.QWidget()
        ui = introduction.Ui_Form()
        ui.setupUi(self.intro)
        self.intro.setFixedSize(self.intro.width(), self.intro.height())

    def setupUi(self, form_base):
        form_base.setObjectName("form_base")
        form_base.resize(781, 465)
        self.label_path = QtWidgets.QLabel(form_base)
        self.label_path.setGeometry(QtCore.QRect(20, 20, 71, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_path.setFont(font)
        self.label_path.setObjectName("label_path")

        self.line_path = QtWidgets.QLineEdit(form_base)
        self.line_path.setGeometry(QtCore.QRect(90, 20, 511, 21))
        self.line_path.setObjectName("line_path")

        self.button_choose_dict = QtWidgets.QPushButton(form_base)
        self.button_choose_dict.setGeometry(QtCore.QRect(620, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.button_choose_dict.setFont(font)
        self.button_choose_dict.setObjectName("button_choose_dict")
        self.button_choose_dict.clicked.connect(self.show_dialog)

        self.botton_refresh = QtWidgets.QPushButton(form_base)
        self.botton_refresh.setGeometry(QtCore.QRect(30, 60, 75, 23))
        self.botton_refresh.setObjectName("botton_refresh")
        self.botton_refresh.clicked.connect(self.show_refresh_data)

        self.table_data = QtWidgets.QTableView(form_base)
        self.table_data.setGeometry(QtCore.QRect(10, 150, 761, 311))
        self.table_data.setObjectName("table_data")
        self.model = QtGui.QStandardItemModel()
        self.table_data.horizontalHeader().setStretchLastSection(True)
        # self.table_data.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table_data.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)
        self.table_data.setModel(self.model)
        self.table_data.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_data.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_data.setAlternatingRowColors(True)
        self.table_data.clicked.connect(self.click_table_row)
        self.table_data.setSortingEnabled(True)
        self.re_init_headers()

        self.label_tips = QtWidgets.QLabel(form_base)
        self.label_tips.setGeometry(QtCore.QRect(120, 80, 551, 51))
        self.label_tips.setText("")
        self.label_tips.setAlignment(QtCore.Qt.AlignCenter)
        self.label_tips.setStyleSheet("color:red")
        self.label_tips.setObjectName("label_tips")

        self.button_export = QtWidgets.QPushButton(form_base)
        self.button_export.setGeometry(QtCore.QRect(30, 90, 75, 23))
        self.button_export.setObjectName("button_export")
        self.button_export.clicked.connect(self.export_table_info)

        self.button_import = QtWidgets.QPushButton(form_base)
        self.button_import.setGeometry(QtCore.QRect(30, 120, 75, 23))
        self.button_import.setObjectName("button_import")
        self.button_import.clicked.connect(self.import_records)

        self.button_introduction = QtWidgets.QPushButton(form_base)
        self.button_introduction.setGeometry(QtCore.QRect(700, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.button_introduction.setFont(font)
        self.button_introduction.setObjectName("button_introduction")
        self.button_introduction.clicked.connect(self.show_introduction)

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
        self.model.setHorizontalHeaderLabels(['时间', '文件名', '职业', '等级', '存档代码'])
        self.table_data.setColumnWidth(0, 140)
        self.table_data.setColumnWidth(1, 120)
        self.table_data.setColumnWidth(2, 60)
        self.table_data.setColumnWidth(3, 60)
        self.table_data.setColumnWidth(4, 340)

    def show_refresh_data(self):
        if regex_controll.check_valid_path(self.chosen_path):
            self.show_archive_info()
            self.save_or_update_records()
        else:
            self.label_tips.setText("请先选择正确的存档目录!")

    def show_archive_info(self):
        global files
        try:
            try:
                files = os.listdir(self.chosen_path)
            except FileNotFoundError as ffe:
                self.label_tips.setText("系统找不到指定的路径，请重新选择正确的存档目录!")
                return
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
            self.model.sort(0, QtCore.Qt.DescendingOrder)
            self.label_tips.setText("单击选择某行信息，便可自动复制存档代码")
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

    def click_table_row(self):
        row = self.table_data.currentIndex().row()
        model = self.table_data.model()
        job = model.index(row, 2)
        degree = model.index(row, 3)
        code = model.index(row, 4)
        self.label_tips.setText(model.data(job) + "（" + model.data(degree) + "）\n" + "存档代码已复制： " + model.data(code))
        self.set_clipboard(model.data(code))

    def set_clipboard(self, text):
        winclb.OpenClipboard()
        winclb.EmptyClipboard()
        winclb.SetClipboardText(text)
        winclb.CloseClipboard()

    def export_table_info(self):
        self.save_or_update_records()
        self.label_tips.setText("已将存档信息导出到该程序所在目录的records.txt中，请查看")

    def save_or_update_records(self):
        model = self.table_data.model()
        row_count = model.rowCount()
        column_count = 5
        f = open("records.txt", "w", encoding="utf-8")
        export_time = t.strftime('%Y-%m-%d %H:%M:%S', t.localtime(t.time()))
        result = str()
        result += "导出时间：" + export_time + "\n" + "-" * 100 + "\n"
        for i in range(row_count):
            for j in range(column_count):
                data = model.index(i, j)
                result += model.data(data)
                result += ","
            result = result[:-1]
            result += "\n"
        f.write(result.strip())
        f.close()

    def import_records(self):
        file_path = "records.txt"
        if os.path.exists(file_path):
            f = open(file_path, "r", encoding="utf-8")
            self.model.clear()
            self.re_init_headers()
            for line in f.readlines():
                lst = line.split(",")
                if len(lst) < 2:
                    continue
                file_modify_time = lst[0]
                file_name = lst[1]
                job = lst[2]
                degree = lst[3]
                code = lst[4]
                self.model.appendRow([QtGui.QStandardItem(file_modify_time),
                                      QtGui.QStandardItem(file_name),
                                      QtGui.QStandardItem(job),
                                      QtGui.QStandardItem(degree),
                                      QtGui.QStandardItem(code)])
            self.model.sort(0, QtCore.Qt.DescendingOrder)
        else:
            self.label_tips.setText("程序所在目录没有找到records.txt文件")

    def show_introduction(self):
        self.intro.show()

    def retranslateUi(self, form_base):
        _translate = QtCore.QCoreApplication.translate
        form_base.setWindowTitle(_translate("form_base", "世界ORPG存取档管理器v1.0 by 执着的小浮云"))
        form_base.setToolTip(_translate("form_base", "<html><head/><body><p><br/></p></body></html>"))
        self.label_path.setText(_translate("form_base", "存档目录"))
        self.button_choose_dict.setText(_translate("form_base", "目录选择"))
        self.botton_refresh.setText(_translate("form_base", "全部刷新"))
        self.button_export.setText(_translate("form_base", "全部导出"))
        self.button_import.setText(_translate("form_base", "全部导入"))
        self.button_introduction.setText(_translate("form_base", "打开说明"))
