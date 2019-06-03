from PyQt5.QtWidgets import QWidget, QSizePolicy, QVBoxLayout

from matplotlib.backends.backend_qt5agg \
    import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


def draw_plot(build_fun):
    def wrapper(self, *args, **kwargs):
        print(*args)
        self.canvas.axes_stat_queue_frequency.clear()
        self.canvas.axes_total_count_fire_put.clear()
        build_fun(self, *args, **kwargs)
        self.canvas.draw()
    return wrapper


class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()

        self.axes_stat_queue_frequency = self.fig.add_subplot(211)
        self.axes_total_count_fire_put = self.fig.add_subplot(212)
        self.customize_axes()

        FigureCanvas.__init__(self, self.fig)
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def customize_axes(self):
        self.fig.subplots_adjust(hspace = 0.6)
        self.axes_stat_queue_frequency.set_title('Queue Frequency')
        self.axes_total_count_fire_put.set_title('Extinguishing Statistics')


class MplStatWidget(QWidget):

    def __init__(self, parent):
        super().__init__(parent)
        self.canvas = MplCanvas()
        self.vbl = QVBoxLayout()
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)

    @draw_plot
    def build_bar(self, clnames, clvalue, cout_of_fire_ok, count_of_fire_bad, grid = True, **kwargs):
        self.canvas.axes_stat_queue_frequency.set_title('Queue Frequency')
        self.canvas.axes_total_count_fire_put.set_title('Extinguishing Statistics')

        self.canvas.axes_stat_queue_frequency.set_xlabel('size of queue')
        self.canvas.axes_stat_queue_frequency.set_ylabel('frequency')

        self.canvas.axes_total_count_fire_put.set_ylabel('count')

        if grid:
            self.canvas.axes_stat_queue_frequency.grid(color = 'b', linestyle = '--',
                                                       linewidth = 0.5, axis = 'y')

            self.canvas.axes_total_count_fire_put.grid(color = 'b',
                                                       linestyle = '--',
                                                       linewidth = 0.5,
                                                       axis = 'y')
        self.canvas.axes_stat_queue_frequency.bar(clnames, clvalue, **kwargs)
        self.canvas.axes_total_count_fire_put.bar(['extinguished', 'not extinguished'],
                                                  [cout_of_fire_ok, count_of_fire_bad], **kwargs)

