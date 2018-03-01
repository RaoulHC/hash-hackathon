# car class file


class Car(object):
    ride_queue = None
    counter = 1

    def __init__(self):
        self.pos = (0, 0)
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
        # check if finished
        if self.finish is True:
            return

        # check if ride
        elif self.ride is not None:
            self.ride_step()
            return

        # find ride
        if Car.ride_queue.is_empty():
            self.finished = True
            return
        self.ride = Car.ride_queue.give_ride(self.pos[0], self.pos[1], self.id)
        if self.ride is None:
            self.is_moving = False

    def ride_step(self):
        pass
