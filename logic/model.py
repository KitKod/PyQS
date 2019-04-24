import simpy
from actors import FireGenerator
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


def start(c_engines):
    env = simpy.Environment()
    fire_station = simpy.Resource(env, capacity = c_engines)
    fire_generator = FireGenerator(2, 6)

    env.process(fire_generator.create_fire(env, fire_station))
    env.run(200)


if __name__ == '__main__':
    start(1)
