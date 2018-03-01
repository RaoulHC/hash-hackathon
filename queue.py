from copy import deepcopy
from car import Car

class RideQueue(object):
    """

    """
    def __init__(self, ride_list):
        """
        """
        self.ride_queue = ride_list
        self.ride_map = {}

    def distance(self, ride, x,y):
        manhat_dist = abs(x - ride.start_pos[0]) + abs(y - ride.start_pos[1])
        # the time a car will wait can be added to the distance between a car
        # and a ride as it can be thought of as an effective additional distance
        wait_distance = min(0,ride.earliest_step - Car.t - manhat_dist)
        return manhat_dist + wait_distance

    def give_ride(sekf, x, y, car_id):
        """
        Give a car located at x,y the closest ride to it

        IMPROVEMENTS:
            1. Only get rides it is possible do
            2.
        """

        # Start with the first ride in the queue as a trial solution.
        best_distance = self.distance(self.ride_queue[0])
        current_ride = 0

        #
        for i in xrange(len(ride_queue)):
            # for each ride evaluate the distance between the car and the ride
            distance_to_car = self.distance(self.ride_queue[i])
            if distance_to_car < best_distance:
                best_distance = distance_to_car
                current_ride = i

        # Store the assigned ride's id to the final list
        if car_id in self.ride_map:
            self.ride_map[car_id].append(ride_queue[current_ride].id)
        else:
            self.ride_map[car_id] = []
            self.ride_map[car_id].append(ride_queue[current_ride].id)

        # copy the ride for return
        return_ride =  deepcopy(ride_queue[current_ride])

        # remove ride from list
        del ride_queue[current_ride]
        return return_ride

    def ride_empty():
        if not ride_queue:
            return false
