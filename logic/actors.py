from .builder import size_queue, time_q


class Fire:

    def __init__(self, id, level, points):
        self.id = id
        self.level = level
        self.points = points

    def burn(self, env, fire_station, putout_delay):
        print('I am #{} burning... Now={}'.format(self.id, env.now))

        with fire_station.request() as req_engine:
            yield req_engine

            # Start put out this fire
            print('Engine #{} start put out me.. Now={}'.format(self.id, env.now))
            print('In queue now is about={}'.format(len(fire_station.queue)))

            size_queue.append(len(fire_station.queue))
            time_q.append(env.now)

            yield env.timeout(putout_delay)
            print('Stop #{} put out me.. Now={}'.format(self.id, env.now))


class FireGenerator:

    def __init__(self, delay):
        self.delay = delay

    def create_fire(self, env, fire_station, putout_delay):
        i = 1
        while True:
            print('Delay', self.delay)

            fire = Fire(i, 10, 11)
            env.process(fire.burn(env, fire_station, putout_delay))
            i += 1

            yield env.timeout(self.delay)


