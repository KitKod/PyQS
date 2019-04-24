import simpy
import random
import numpy
from scipy.stats import truncnorm
import matplotlib.pyplot as plt

def car(env, name, r):
    yield env.timeout(2)

    print('request for resource %s' % name)

    with r.request() as req:
        yield req
        print('using resourse... req=%s' % req)
        # while True:
        #     pass
        print('leave resourse...')

        yield env.timeout(10)
        print('A-1 = %s' % r.put_queue)
        print('A-2 = %s' % len(r.queue))



if __name__ == '__main__':

    # env = simpy.Environment()
    #
    # r = simpy.Resource(env, capacity = 1)
    # # r.get_queue
    # for i in range(4):
    #     env.process(car(env, 'Car %d' % i, r))
    #
    # env.run()


    # range = -7
    # range2 = 7
    #
    # scale = (range2 - range) / 2
    # size = 5000
    #
    # X = truncnorm(a = range / scale, b = range2 / scale, scale = scale).rvs(
    #     size = size)
    #
    # print(X)
    #
    # X = X.round().astype(int)
    #
    # print(X)
    #
    # bins = 2 * range2 + 1
    # plt.hist(X, bins)
    # plt.show()
    # print(numpy.random.normal(loc = 0, scale = 5, size = 6))
    # for i in range(6):
    #     print(random.gauss(mu = 0, sigma = 5))


    # x = random.gauss(mu = (5 - 3) / 2, sigma = )

    for i in range(200):

        r = i + random.randint(5, 17)
        scale = (r + i) / 2

        delay = truncnorm(a = i / scale,
                          b = r / scale,
                          scale = scale).rvs().round().astype(int)

        print('A', r, i)
        if i <= delay <= r:
            print('True', delay)
            pass
        else:
            print('False', delay)