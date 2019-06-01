from Defs import StatisticHolder


def show_graph(mui):
    stat_holder = StatisticHolder.getInstance()
    mui.mpl.build_plot(stat_holder.time_q, stat_holder.size_queue)
    stat_holder.clear_stat()



# def build_plot(mui):
#     count = 6
#
#     if count > 50:
#         msg_box = QMessageBox()
#         msg_box.setText("You have entered a very large value in the count field. \n"
#                         "The maximum possible value is 50.")
#         msg_box.exec()
#     else:
#         mui.mpl.build_hist()
