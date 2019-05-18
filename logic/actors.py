from .builder import size_queue, time_q
import random


class Engine:

    def __init__(self):
        pass


class Fire:

    def __init__(self, id, burning_time):
        self.id = id
        self.burning_time = burning_time  ## Сможет ли машина потушить пожар.

    def burn(self, env, fire_station, serv_max, serv_min):
        print('I am #{} burning... Now={}'.format(self.id, env.now))


        size_queue.append(len(fire_station.queue))
        time_q.append(env.now)
        print("TEST", len(fire_station.queue))
        with fire_station.request() as req_engine:
            yield req_engine

            # Start put out this fire
            print('Engine #{} start put out me.. Now={}'.format(self.id, env.now))
            print('In queue now is about={}'.format(len(fire_station.queue)))

            size_queue.append(len(fire_station.queue))
            time_q.append(env.now)

            yield env.timeout(random.randint(serv_min, serv_max))
            print('Stop #{} put out me.. Now={}'.format(self.id, env.now))


class FireGenerator:

    def __init__(self, fire_inter_max, fire_inter_min, burn_time_max,
                 burn_time_min):
        self.fire_inter_max = fire_inter_max
        self.fire_inter_min = fire_inter_min
        self.burn_time_max = burn_time_max
        self.burn_time_min = burn_time_min

    def create_fire(self, env, fire_station, serv_max, serv_min):
        i = 1
        while True:
            burning_time = random.randint(self.burn_time_min,
                                          self.burn_time_max)
            if burning_time <= 0:
                burning_time = self.burn_time_max

            fire = Fire(i, burning_time)
            env.process(fire.burn(env, fire_station, serv_max, serv_min))

            delay = random.randint(self.fire_inter_min, self.fire_inter_max)
            if delay <= 0:
                delay = self.fire_inter_max

            print('Delay={}; burning={}', delay, burning_time)
            i += 1

            yield env.timeout(delay)


