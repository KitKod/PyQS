import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.qtview import Ui_MplMainWindow
from logic import builder
from Defs import DISTRIBUTION_LAWS


class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mui = Ui_MplMainWindow()
        self.mui.setupUi(self)
        self.init_signals()
        self.init_widgets()

    def init_signals(self):
        self.mui.button_start_test.clicked.connect(
            lambda: builder.build_plot(self.mui)
        )
        # self.mui.comboBox_inter_fires.

    def init_widgets(self):
        self.mui.comboBox_inter_fires.addItems(DISTRIBUTION_LAWS)
        self.mui.comboBox_time_of_putout.addItems(DISTRIBUTION_LAWS)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startWindow = StartWindow()
    startWindow.show()
    sys.exit(app.exec_())
