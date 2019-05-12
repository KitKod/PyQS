from logic.model import Test
from logic.builder import size_queue, time_q


def launch_test(mui):
    total_engines = int(mui.LEdit_total_fire_engines.text())
    model_time = int(mui.LEdit_time_of_modeling.text())

    fire_inter_max = int(mui.LEdit_dist_fireinter_max.text())
    fire_inter_min = int(mui.LEdit_dist_fireinter_min.text())

    burn_time_max = int(mui.LEdit_dist_burntime_max.text())
    burn_time_min = int(mui.LEdit_dist_burntime_min.text())

    cnt_big_engin = int(mui.LEdit_count_big_engines.text())
    cnt_average_engin = int(mui.LEdit_count_average_engines.text())
    cnt_small_engin = int(mui.LEdit_count_small_engines.text())

    test = Test(total_engines, model_time, fire_inter_max, fire_inter_min,
                burn_time_max, burn_time_min, cnt_big_engin,
                cnt_average_engin, cnt_small_engin)

    test.run()

    mui.mpl.build_bar(time_q, size_queue)
    size_queue.clear()
    time_q.clear()

