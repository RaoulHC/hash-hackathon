# car class file


class Car(object):
    ride_queue = []
    counter = 1

    def __init__(self):
        self.ride = None
        self.finish = False
        self.is_moving = True
        self.id = Car.counter
        Car.counter += 1

    @classmethod
    def initialise_ride_queue(cls, queue):
        cls.ride_queue = queue

    def get_ride_queue(self):
        return Car.ride_queue

    def step(self):
        if Car.ride_queue == []:
            self.finish = True
            return
