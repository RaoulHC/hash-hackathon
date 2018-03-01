# car class file


class Car(object):
    ride_queue = []

    def __init__(self):
        self.ride = None
        self.finish = False
        self.is_moving = True

    @classmethod
    def initialise_ride_queue(cls, queue):
        cls.ride_queue = queue

    def get_ride_queue(self):
        return Car.ride_queue

    def step(self):
        if Car.ride_queue == []:
            self.finish = True
            return
