import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.qtview import Ui_MplMainWindow
import random
from collections import Counter

class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mui = Ui_MplMainWindow()
        self.mui.setupUi(self)
        self.init_signals()

    def init_signals(self):
        self.mui.button_build.clicked.connect(self.build_plot)

    def build_plot(self):
        max = int(self.mui.lineEdit_max.text())
        min = int(self.mui.lineEdit_min.text())
        count = int(self.mui.lineEdit_count.text())

        lable = Counter([random.randint(min, max) for i in range(count)])
        print('lable=', lable)

        names, value = list(), list()
        for k, v in lable.items():
            names.append(str(k))
            value.append(v)
        self.mui.mpl.set_axes(xarray=names, yarray=value)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startWindow = StartWindow()
    startWindow.show()
    sys.exit(app.exec_())
