import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.qtview import Ui_MplMainWindow
from control import launch_test


class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mui = Ui_MplMainWindow()
        self.mui.setupUi(self)
        self.init_widgets()
        self.init_signals()

    def init_signals(self):
        self.mui.button_start_test.clicked.connect(
            lambda: launch_test(self.mui)
        )

    def init_widgets(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startWindow = StartWindow()
    startWindow.show()
    sys.exit(app.exec_())

