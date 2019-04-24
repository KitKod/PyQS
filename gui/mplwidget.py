from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout

from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def draw_plot(build_fun):
    def wrapper(self, *args, **kwargs):
        print(*args)
        self.canvas.axes.clear()
        build_fun(self, *args, **kwargs)
        self.canvas.draw()
    return wrapper


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.axes = self.fig.add_subplot(111)

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

    @draw_plot
    def build_bar(self, clnames, clvalue, grid=True, **kwargs):
        if grid:
            self.canvas.axes.grid(color='b', linestyle='--', linewidth=0.5)
        self.canvas.axes.bar(clnames, clvalue, **kwargs)

    @draw_plot
    def build_hist(self):
        x = [1, 2, 3, 4, 1, 1 , 1]
        num_bins = 6
        self.canvas.axes.hist(x, align='left')
