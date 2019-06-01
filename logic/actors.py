import random
from Defs import StatisticHolder


class FireStation:

    def __init__(self, env, container, engn_park):
        self.env = env
        self.stat_holder = StatisticHolder.getInstance()
        self.container = container
        self.engn_park = engn_park

    def register_fire(self, fire, serv_max, serv_min):
        print('New Fire was created ID={}; TIME={}'.format(fire.id, self.env.now))
        self.stat_holder.collect_queue_info(len(self.container.get_queue),
                                            self.env.now)

        busy_engn = self.load_mediator(fire)
        yield self.container.get(busy_engn)
        ## If the container has enough resource, the process will continue

        print('DEBUG SIZEQ={}; BUSYCARS={}; INCONT={}'.format(len(self.container.get_queue),
                                                              busy_engn,
                                                              self.container.level))

        self.put_out_fire(fire)
        yield self.env.timeout(random.randint(serv_min, serv_max))
        print('Station has finished putting out the fire ID={}\n'.format(fire.id))
        self.container.put(busy_engn)

    def load_mediator(self, fire):
        ## TODO: We need to determine how many cars should go to the call.
        return 2

    def put_out_fire(self, fire):
        print('Station start put out the fire ID={}'.format(fire.id))
        self.stat_holder.collect_queue_info(len(self.container.get_queue),
                                            self.env.now)


class Engine:

    def __init__(self):
        pass


class Fire:

    def __init__(self, id, burning_time):
        self.id = id
        self.burning_time = burning_time  ## Сможет ли машина потушить пожар.


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
            # env.process(fire.burn(env, fire_station, serv_max, serv_min))
            env.process(fire_station.register_fire(fire, serv_max, serv_min))

            delay = random.randint(self.fire_inter_min, self.fire_inter_max)
            if delay <= 0:
                delay = self.fire_inter_max

            print('Fire Generator delay={}; burning={}'.format(delay,
                                                               burning_time))
            i += 1

            yield env.timeout(delay)


