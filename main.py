from PyQt5 import QtWidgets

# python cxfreeze e:\pyproject\archive-management\main.py --target-dir E:\myexe --base-name="win32gui"

import menu_actual
import sys
from PyQt5.QtGui import QIcon

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = menu_actual.Ui_form_base()
    ui.setupUi(widget)
    ui.initUiRight()
    widget.setWindowIcon(QIcon('web.png'))  # 增加icon图标，如果没有图片可以没有这句
    widget.setFixedSize(widget.width(), widget.height())
    widget.show()
    sys.exit(app.exec_())
