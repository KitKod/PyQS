from PyQt5.QtWidgets import QMessageBox

from .model import random_state


def build_plot(mui):
    max = int(mui.lineEdit_count_fire_engine.text())
    min = int(mui.lineEdit_time_of_modeling.text())
    count = 6

    if count > 50:
        msg_box = QMessageBox()
        msg_box.setText("You have entered a very large value in the count field. \n"
                        "The maximum possible value is 50.")
        msg_box.exec()
    else:
        mui.mpl.build_bar(*random_state(min, max, count))
