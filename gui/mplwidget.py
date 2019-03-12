from PyQt5 import QtGui
from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout

from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)
        # self.axes.plot([0, 5], [5, 8])

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)


class MplWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = MplCanvas()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    def set_axes(self, xarray='', yarray='', *args):
        self.canvas.axes.clear()
        self.canvas.axes.bar(xarray, yarray, *args)
        self.canvas.draw()


