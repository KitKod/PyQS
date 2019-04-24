from scipy.stats import truncnorm


class Fire:

    def __init__(self, id, level, points):
        self.id = id
        self.level = level
        self.points = points

    def burn(self, env, fire_station):
        print('I am #{} burning... Now={}'.format(self.id, env.now))

        with fire_station.request() as req_engine:
            yield req_engine

            # Start put out this fire
            print('Engine #{} start put out me.. Now={}'.format(self.id, env.now))
            print('In queue now is about={}'.format(len(fire_station.queue)))
            yield env.timeout(24)
            print('Stop #{} put out me.. Now={}'.format(self.id, env.now))


class FireGenerator:

    def __init__(self, min_edge, max_edge):
        self.min_edge = min_edge
        self.max_edge = max_edge

    def create_fire(self, env, fire_station):
        i = 1
        while True:
            scale = (self.max_edge + self.min_edge) / 2
            delay = truncnorm(a = self.min_edge / scale,
                              b = self.max_edge / scale,
                              scale = scale).rvs().round().astype(int)
            print('Delay', delay)

            fire = Fire(i, 10, 11)
            env.process(fire.burn(env, fire_station))
            i += 1

            yield env.timeout(delay)


