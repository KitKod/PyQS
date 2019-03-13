from .model import random_state


def build_plot(mui):
    max = int(mui.lineEdit_max.text())
    min = int(mui.lineEdit_min.text())
    count = int(mui.lineEdit_count.text())

    mui.mpl.build_bar(*random_state(min, max, count))
