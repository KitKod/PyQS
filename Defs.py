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

    def collect_queue_info(self, size, time):
        self.size_queue.append(size)
        self.time_q.append(time)

    def clear_stat(self):
        self.size_queue.clear()
        self.time_q.clear()

