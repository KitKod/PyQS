from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout

from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def draw_plot(build_fun):
    def wrapper(self, *args, **kwargs):
        print(*args)
        self.canvas.axes_queue_time.clear()
        self.canvas.axes_putout.clear()
        build_fun(self, *args, **kwargs)
        self.canvas.draw()
    return wrapper


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        self.axes_queue_time = self.fig.add_subplot(211)
        self.axes_putout = self.fig.add_subplot(212)
        self.customize_axes()

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def customize_axes(self):
        self.fig.subplots_adjust(hspace = 0.6)
        self.axes_queue_time.set_title('Queue-Time')
        self.axes_putout.set_title('Extinguished/Not-Extinguished')


class MplWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = MplCanvas()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    @draw_plot
    def build_plot(self, clnames, clvalue, x_putout_queue, y_putout_count,
                   x_putout_queue_ok, y_putout_count_ok, grid=True, **kwargs):
        if grid:
            self.canvas.axes_queue_time.grid(color= 'b', linestyle= '--',
                                             linewidth=0.5)
            self.canvas.axes_putout.grid(color = 'b', linestyle = '--',
                                             linewidth = 0.5)
        self.canvas.axes_queue_time.set_title('Queue-Time')
        self.canvas.axes_queue_time.set_xlabel('time')
        self.canvas.axes_queue_time.set_ylabel('size queue')

        self.canvas.axes_putout.set_title('Extinguished/Not-Extinguished')
        self.canvas.axes_putout.set_xlabel('time')
        self.canvas.axes_putout.set_ylabel('count')

        self.canvas.axes_queue_time.plot(clnames, clvalue, **kwargs)
        self.canvas.axes_putout.plot(x_putout_queue, y_putout_count, 'r',
                                     x_putout_queue_ok, y_putout_count_ok, 'b')

    @draw_plot
    def build_bar(self, clnames, clvalue, grid = True, **kwargs):
        if grid:
            self.canvas.axes_queue_time.grid(color = 'b', linestyle = '--',
                                             linewidth = 0.5)
        self.canvas.axes_queue_time.bar(clnames, clvalue, **kwargs)

