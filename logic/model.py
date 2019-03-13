import simpy
import random
from collections import Counter


def random_state(min, max, count):
    lable = Counter([random.randint(min, max) for i in range(count)])
    print('lable=', lable)

    names, values = list(), list()
    for k, v in lable.items():
        names.append(str(k))
        values.append(v)
    return names, values
