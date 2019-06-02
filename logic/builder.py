from Defs import StatisticHolder
from collections import Counter
from PyQt5.QtWidgets import QMessageBox


def show_graph(mui):
    stat_holder = StatisticHolder.getInstance()
    mui.mpl.build_plot(stat_holder.time_q, stat_holder.size_queue,
                       stat_holder.time_fire_bad, stat_holder.count_fire_bad,
                       stat_holder.time_fire_ok, stat_holder.count_fire_ok)


def show_stat_graphs(mui):
    stat_holder = StatisticHolder.getInstance()
    freq = dict(Counter(stat_holder.size_queue))
    names, values = list(), list()
    for k, v in freq.items():
        names.append(str(k))
        values.append(v)

    count_fire_ok = stat_holder.count_fire_ok[-1] if stat_holder.count_fire_ok else 0
    count_fire_bad = stat_holder.count_fire_bad[-1] if stat_holder.count_fire_bad else 0
    print('ok={}; bad={}'.format(count_fire_ok, count_fire_bad))
    mui.mpl_stat.build_bar(names, values, count_fire_ok, count_fire_bad)
    stat_holder.clear_stat()


def user_warning(msg):
    msg_box = QMessageBox()
    msg_box.setText(msg)
    msg_box.exec()

