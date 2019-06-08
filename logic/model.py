import simpy
from .actors import FireGenerator, FireStation, EngineManager


class Test:

    def __init__(self, total_engines, model_time, fire_inter_max,
                 burn_time_max, burn_time_min, cnt_big_engin,
                 cnt_average_engin, cnt_small_engin, serv_max, serv_min):

        self.total_engines = total_engines
        self.model_time = model_time
        self.fire_inter_max = fire_inter_max
        self.burn_time_max = burn_time_max
        self.burn_time_min = burn_time_min
        self.cnt_big_engin = cnt_big_engin
        self.cnt_average_engin = cnt_average_engin
        self.cnt_small_engin = cnt_small_engin
        self.serv_max = serv_max
        self.serv_min = serv_min

    def run(self):
        env = simpy.Environment()
        container = simpy.Container(env, capacity = self.total_engines,
                                        init = self.total_engines)
        engn_manager = EngineManager(env, container,
                                     self.burn_time_max,
                                     self.burn_time_min,
                                     self.cnt_big_engin,
                                     self.cnt_average_engin,
                                     self.cnt_small_engin)
        fire_station = FireStation(env, engn_manager)
        fire_generator = FireGenerator(self.fire_inter_max,
                                       self.burn_time_max,
                                       self.burn_time_min)
        env.process(fire_generator.create_fire(env, fire_station,
                                               self.serv_max,
                                               self.serv_min))
        env.run(self.model_time)
