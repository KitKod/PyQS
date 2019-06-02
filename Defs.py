class StatisticHolder:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if StatisticHolder.__instance is None:
            StatisticHolder()
        return StatisticHolder.__instance

    def __init__(self):
        if StatisticHolder.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            StatisticHolder.__instance = self
        self.size_queue = list()
        self.time_q = list()

        self.count_fire_ok = list()
        self.time_fire_ok = list()

        self.count_fire_bad = list()
        self.time_fire_bad = list()

    def collect_stat_fire_ok(self, time):
        if len(self.count_fire_ok) == 0:
            self.count_fire_ok.append(1)
        else:
            last = self.count_fire_ok[-1] + 1
            self.count_fire_ok.append(last)
        self.time_fire_ok.append(time)

    def collect_stat_fire_bad(self, time):
        if len(self.count_fire_bad) == 0:
            self.count_fire_bad.append(1)
        else:
            last = self.count_fire_bad[-1] + 1
            self.count_fire_bad.append(last)
        self.time_fire_bad.append(time)

    def collect_queue_info(self, size, time):
        self.size_queue.append(size)
        self.time_q.append(time)

    def clear_stat(self):
        self.size_queue.clear()
        self.time_q.clear()

        self.count_fire_bad.clear()
        self.time_fire_bad.clear()

        self.count_fire_ok.clear()
        self.time_fire_ok.clear()

