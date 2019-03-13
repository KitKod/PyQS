import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from gui.qtview import Ui_MplMainWindow
from logic import builder


class StartWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.mui = Ui_MplMainWindow()
        self.mui.setupUi(self)
        self.init_signals()

    def init_signals(self):
        self.mui.button_build.clicked.connect(
            lambda: builder.build_plot(self.mui)
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    startWindow = StartWindow()
    startWindow.show()
    sys.exit(app.exec_())
