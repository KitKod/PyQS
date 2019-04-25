import simpy
from .actors import FireGenerator
import random
from collections import Counter

#
# def random_state(min, max, count):
#     lable = Counter([random.randint(min, max) for i in range(count)])
#     print('lable=', lable)
#
#     names, values = list(), list()
#     for k, v in lable.items():
#         names.append(str(k))
#         values.append(v)
#     return names, values


def test(cnt_engines, model_time, fire_delay, putout_delay):
    env = simpy.Environment()
    fire_station = simpy.Resource(env, capacity = cnt_engines)
    fire_generator = FireGenerator(fire_delay)

    env.process(fire_generator.create_fire(env, fire_station, putout_delay))
    env.run(model_time)



def stat():
    pass


def regres():
    pass


def transient():
    pass


if __name__ == '__main__':
    test(1)
