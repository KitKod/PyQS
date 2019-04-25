from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, QDialog, QPushButton
from logic.model import test
import random
from logic.builder import size_queue, time_q


class StartData:
    def __init__(self, fire, putout):
        # self.fire_delay = fire_delay
        # self.putout_delay = putout_delay

        self.fire_mu = fire[0]
        self.fire_range = fire[1]

        self.putout_mu = putout[0]
        self.putout_range = putout[1]

    def set_fire_value(self, fire, i):
        self.fire_mu = fire[0]
        self.fire_range = fire[1]
        i.close()

    def set_putout_value(self, putout, i):
        self.putout_mu = putout[0]
        self.putout_range = putout[1]
        i.close()

    def set_fire_delay(self):
        tmp = int(random.gauss(self.fire_mu, self.fire_range))
        if tmp < 0:
            tmp = tmp * -1
        elif tmp == 0:
            tmp = tmp + 1
        return tmp

    def set_putout_delay(self):
        tmp = int(random.gauss(self.putout_mu, self.putout_range))
        if tmp < 0:
            tmp = tmp * -1
        elif tmp == 0:
            tmp = tmp + 1
        return tmp


sd = StartData((1, 5), (2, 10))


def show_dialog(mui, mode):
    layout = QVBoxLayout()
    le_mu = QLineEdit()
    le_range = QLineEdit()
    button_ok = QPushButton('Ok')
    button_cancel = QPushButton('Cancel')

    layout.addWidget(le_mu)
    layout.addWidget(le_range)
    layout.addWidget(button_ok)
    layout.addWidget(button_cancel)

    i = QDialog()
    i.setLayout(layout)

    if mode == 0:
        button_ok.clicked.connect(lambda: sd.set_fire_value((int(le_mu.text()), int(le_range.text())), i))
    else:
        button_ok.clicked.connect(lambda: sd.set_putout_value((int(le_mu.text()), int(le_range.text())), i))

    button_cancel.clicked.connect(lambda: i.close())
    i.exec()


def launch_test(mui):
    cnt_engines = int(mui.lineEdit_count_fire_engine.text())
    model_time = int(mui.lineEdit_time_of_modeling.text())

    fire_dist = mui.comboBox_inter_fires.currentIndex()
    time_po_dist = mui.comboBox_time_of_putout.currentIndex()

    print("AAA", sd.set_fire_delay(), sd.set_putout_delay())
    test(cnt_engines, model_time, sd.set_fire_delay(), sd.set_putout_delay())
    mui.mpl.build_bar(time_q, size_queue)
    size_queue.clear()
    time_q.clear()

