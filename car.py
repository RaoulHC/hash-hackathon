# car class file


class Car(object):
    ride_queue = None
    counter = 1
    time = 0

    def __init__(self):
        self.pos = (0, 0)
        self.ride = None
        self.riding = False
        self.time_remaining = 0
        self.finish = False
        self.is_moving = False
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

        # find ride
        if Car.ride_queue.ride_empty():
            self.finished = True
            return

        self.ride = Car.ride_queue.give_ride(self.pos[0], self.pos[1], self.id)
        if self.ride is not None:
            self.time_remaining = self.ride.distance2start(self.pos)
        else:
            self.is_moving = False

        # check if ride
        if self.ride is not None:
            self.ride_step()

    def ride_step(self):
        # if not got ride count down time remaining to pick up
        if self.riding is False:
            self.time_remaining -= 1
            if self.time_remaining == 0:
                self.riding = True
                self.pos = self.ride.start_pos
                self.time_remaining = self.ride.ride_length

        # if got ride
        else:
            self.time_remaining -= 1
            if self.time_remaining == 0:
                self.ride = None
                self.riding = False
                self.pos = self.ride.end_pos
