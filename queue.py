from copy import deepcopy
# queue class file

class RideQueue(object):
    """

    """
    def __init__(self, ride_list):
        """
        """
        self.ride_queue = ride_list
        self.ride_map = {}

    def give_ride(x, y, car_id):
        """
        Give a car located at x,y the closest ride to it
        """

        # Start with the first ride in the queue as a trial solution.
        best_distance = abs(x - ride_queue[0].start_pos[0]) + abs(y - ride_queue[0].start_pos[1])
        current_ride = 0

        #
        for i in xrange(len(ride_queue)):
            # for each ride evaluate the distance between the car and the ride
            distance_to_car = abs(x - ride_queue[i].start_pos[0]) + abs(y - ride_queue[i].start_pos[1])
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
