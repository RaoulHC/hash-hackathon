# car class file


class Car(object):
    ride_queue = []

    def __init__(self):
        self.ride = None
        self.finish = False
        self.is_moving = True

    @staticmethod
    def initialise_ride_queue(cls, queue):
        ride_queue = queue

    def step(self):
        if ride_queue == []:
            self.finish = True
