import simpy


class Car(object):
    def __init__(self, env, rs, name, duration):
        self.env = env
        self.rs = rs
        self.name = name
        self.dr = duration
        self.action = env.process(self.run())

    def run(self):
        yield self.env.timeout(self.dr)
        print('Arrived {} at station about {}'.format(self.name, self.env.now))

        with self.rs.request() as req:
            yield req

            print('Start {} charge about {}'.format(self.name, self.env.now))
            yield self.env.timeout(10)

            print('Leave {} the station about {}'.format(self.name, self.env.now))


if __name__ == '__main__':
    env = simpy.Environment()
    resource = simpy.Resource(env, capacity = 1)
    env.process()
    for i in range(4):
        car = Car(env, resource, i, i*2)

    env.run()
