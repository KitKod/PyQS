import simpy
from .actors import FireGenerator


class Test:

    def __init__(self, total_engines, model_time, fire_inter_max,
                 fire_inter_min, burn_time_max, burn_time_min, cnt_big_engin,
                 cnt_average_engin, cnt_small_engin):

        self.total_engines = total_engines
        self.model_time = model_time
        self.fire_inter_max = fire_inter_max
        self.fire_inter_min = fire_inter_min
        self.burn_time_max = burn_time_max
        self.burn_time_min = burn_time_min
        self.cnt_big_engin = cnt_big_engin
        self.cnt_average_engin = cnt_average_engin
        self.cnt_small_engin = cnt_small_engin

    def run(self):
        env = simpy.Environment()
        fire_station = simpy.Resource(env, capacity = self.total_engines)
        fire_generator = FireGenerator(self.fire_inter_max,
                                       self.fire_inter_min,
                                       self.burn_time_max,
                                       self.burn_time_min)

        env.process(fire_generator.create_fire(env, fire_station))
        env.run(self.model_time)


def stat():
    pass


def regres():
    pass


def transient():
    pass

