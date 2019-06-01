import simpy
from .actors import FireGenerator, FireStation, Engine


class Test:

    def __init__(self, total_engines, model_time, fire_inter_max,
                 fire_inter_min, burn_time_max, burn_time_min, cnt_big_engin,
                 cnt_average_engin, cnt_small_engin, serv_max, serv_min):

        self.total_engines = total_engines
        self.model_time = model_time
        self.fire_inter_max = fire_inter_max
        self.fire_inter_min = fire_inter_min
        self.burn_time_max = burn_time_max
        self.burn_time_min = burn_time_min
        self.cnt_big_engin = cnt_big_engin
        self.cnt_average_engin = cnt_average_engin
        self.cnt_small_engin = cnt_small_engin
        self.serv_max = serv_max
        self.serv_min = serv_min

    def create_engn_park(self, cnt_big, cnt_avg, cnt_small):
        return {
            'bigs': [Engine() for e in range(cnt_big)],
            'avgs': [Engine() for e in range(cnt_avg)],
            'smalls': [Engine() for e in range(cnt_small)]
        }


    def run(self):
        env = simpy.Environment()
        container = simpy.Container(env, capacity = self.total_engines,
                                        init = self.total_engines)

        fire_station = FireStation(env, container,
                                   self.create_engn_park(self.cnt_big_engin,
                                                         self.cnt_average_engin,
                                                         self.cnt_small_engin))

        fire_generator = FireGenerator(self.fire_inter_max,
                                       self.fire_inter_min,
                                       self.burn_time_max,
                                       self.burn_time_min)

        env.process(fire_generator.create_fire(env, fire_station,
                                               self.serv_max,
                                               self.serv_min))
        env.run(self.model_time)


def stat():
    pass


def regres():
    pass


def transient():
    pass

