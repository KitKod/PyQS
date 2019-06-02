import random
from Defs import StatisticHolder


class EngineManager:

    def __init__(self, env, container, max_water, min_water, big_engn, avg_engn,
                 small_engn):
        self.container = container
        self.env = env
        self.stat_holder = StatisticHolder.getInstance()

        self.total_big_engn = big_engn
        self.total_avg_engn = avg_engn
        self.total_small_engn = small_engn

        self.water_in_big = max_water
        self.water_in_avg = int((max_water + min_water) / 2)
        self.water_in_small = min_water

        self.engn_park = {
            'bigs': big_engn,
            'avgs': avg_engn,
            'smalls': small_engn
        }

    def allocate_engns(self, fire):
        ## TODO: We need to determine how many cars should go to the call.
        time_burning = fire.burning_time
        b_water = self.water_in_big
        a_water = self.water_in_avg
        s_water = self.water_in_small

        park = self.engn_park
        engs_on_mission = {}

        def send_one_by_level():
            if a_water < time_burning <= b_water and park['bigs'] > 0:
                park.update({'bigs': park['bigs'] - 1})
                engs_on_mission.update({'bigs': 1})
                return True
            elif s_water < time_burning <= a_water and park['avgs'] > 0:
                park.update({'avgs': park['avgs'] - 1})
                engs_on_mission.update({'avgs': 1})
                return True
            elif time_burning == s_water and park['smalls'] > 0:
                park.update({'smalls': park['smalls'] - 1})
                engs_on_mission.update({'smalls': 1})
                return True
            return False

        def sends_engns_one_type(type, count):
            park.update({type: park[type] - count})
            engs_on_mission.update({type: count})

        if send_one_by_level() is True:
            self.stat_holder.collect_stat_fire_ok(self.env.now)
            return False, engs_on_mission, self.container.get(
                sum(engs_on_mission.values()))

        if park['bigs'] > 0:
            sends_engns_one_type('bigs', 1)
            self.stat_holder.collect_stat_fire_ok(self.env.now)
            return False, engs_on_mission, self.container.get(
                sum(engs_on_mission.values()))

        ## значи тут нету точной машины для тушения пожара в одиночку отправляем как минимум две машиины.
        ## Определяем где еще есть машины.

        in_level = list()

        if park['bigs'] == 0 and park['avgs'] == 0 and park['smalls'] == 0:
            # return None, None
            if a_water < time_burning <= b_water:
                ## Возможна оптимизация. Пока так для поднятия вероятности не потушенных пожаров
                engs_on_mission.update({'bigs': 1})
                self.stat_holder.collect_stat_fire_ok(self.env.now)
                return True, engs_on_mission, self.container.get(1)
            elif s_water < time_burning <= a_water:
                engs_on_mission.update({'avgs': 1})
                self.stat_holder.collect_stat_fire_ok(self.env.now)
                return True, engs_on_mission, self.container.get(1)
            elif time_burning == s_water:
                engs_on_mission.update({'smalls': 1})
                self.stat_holder.collect_stat_fire_ok(self.env.now)
                return True, engs_on_mission, self.container.get(1)
        for k, v in park.items():
            if v != 0:
                in_level.append(k)

        water_in_all_s = 0
        water_in_all_a = 0
        if 'smalls' in in_level:
            water_in_all_s = park['smalls'] * s_water
        if 'avgs' in in_level:
            water_in_all_a = park['avgs'] * a_water

        if water_in_all_s >= time_burning:
            cnt_s_to_go = int(water_in_all_s / time_burning)
            sends_engns_one_type('smalls', cnt_s_to_go)
            self.stat_holder.collect_stat_fire_ok(self.env.now)
            return False, engs_on_mission, self.container.get(
                sum(engs_on_mission.values()))
        elif water_in_all_a >= time_burning:
            cnt_a_to_go = int(water_in_all_a / time_burning)
            sends_engns_one_type('avgs', cnt_a_to_go)
            self.stat_holder.collect_stat_fire_ok(self.env.now)
            return False, engs_on_mission, self.container.get(
                sum(engs_on_mission.values()))
        else:
            all_water = water_in_all_s + water_in_all_a
            if all_water >= time_burning:
                counter = 0
                a = 0
                s = 0
                while counter <= time_burning:
                    if park['avgs'] != 0:
                        counter += a_water
                        park.update({'avgs': park['avgs'] - 1})
                        a += 1
                        engs_on_mission.update({'avgs': a})
                        print('BSUM e={}'.format(engs_on_mission))
                    elif park['smalls'] != 0:
                        counter += s_water
                        park.update({'smalls': park['smalls'] - 1})
                        s += 1
                        engs_on_mission.update({'smalls': s})
                        print('BSUM e={}'.format(engs_on_mission))
                print('park={}; SUM={}'.format(park, sum(engs_on_mission.values())))
                self.stat_holder.collect_stat_fire_ok(self.env.now)
                return False, engs_on_mission, self.container.get(
                    sum(engs_on_mission.values()))
            else:
                ## пожар точно будет не потушен но отправим всех
                self.stat_holder.collect_stat_fire_bad(self.env.now)
                engs_on_mission.update({'smalls': park['smalls']})
                engs_on_mission.update({'avgs': park['avgs']})
                park.update({'smalls': 0})
                park.update({'avgs': 0})
                return False, engs_on_mission, self.container.get(
                    sum(engs_on_mission.values()))

    def release_engns(self, empty, engs_from_mission):
        if not empty:
            for k, v in engs_from_mission.items():
                if k == 'bigs':
                    self.engn_park.update({'bigs': self.engn_park['bigs'] + v})
                elif k == 'avgs':
                    self.engn_park.update({'avgs': self.engn_park['avgs'] + v})
                elif k == 'smalls':
                    self.engn_park.update({'smalls': self.engn_park['smalls'] + v})
        self.container.put(sum(engs_from_mission.values()))


class FireStation:

    def __init__(self, env, engn_manager):
        self.env = env
        self.stat_holder = StatisticHolder.getInstance()
        self.engn_manager = engn_manager

    def register_fire(self, fire, serv_max, serv_min):
        print('New Fire was created ID={}; TIME={}'.format(fire.id, self.env.now))
        self.stat_holder.collect_queue_info(len(self.engn_manager.container.get_queue),
                                            self.env.now)

        empty, engns_on_mission, request = self.engn_manager.allocate_engns(fire)
        # while engns_on_mission is None and request is None:
        #     yield self.env.timeout(10)
        #     engns_on_mission, request = self.engn_manager.allocate_engns(fire)
        yield request
        ## If the container has enough resource, the process will continue

        flag = True
        if empty:
            while self.engn_manager.engn_park[list(engns_on_mission.keys())[0]] == 0:
                if flag:
                    self.stat_holder.collect_queue_info(
                        len(self.engn_manager.container.get_queue),
                        self.env.now)
                    flag = False
                yield self.env.timeout(5)
            flag = True


        print('DEBUG SIZEQ={}; BUSYCARS={}; INCONT={}'
              .format(len(self.engn_manager.container.get_queue),
                      engns_on_mission,
                      self.engn_manager.container.level))

        self.put_out_fire(fire)
        yield self.env.timeout(random.randint(serv_min, serv_max))

        print('Station has finished putting out the fire ID={}\n'.format(fire.id))
        self.engn_manager.release_engns(empty, engns_on_mission)

    def put_out_fire(self, fire):
        print('Station start put out the fire ID={}'.format(fire.id))
        self.stat_holder.collect_queue_info(len(self.engn_manager.container.get_queue),
                                            self.env.now)


class Engine:

    def __init__(self, type, count, water_tank):
        self.water_tank = water_tank


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
            env.process(fire_station.register_fire(fire, serv_max, serv_min))

            delay = random.randint(self.fire_inter_min, self.fire_inter_max)
            if delay <= 0:
                delay = self.fire_inter_max

            print('Fire Generator delay={}; burning={}'.format(delay,
                                                               burning_time))
            i += 1

            yield env.timeout(delay)
