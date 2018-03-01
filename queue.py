from copy import deepcopy
# queue class file

class queue(object):

    def __init__(self, ride_list, car_list):
        self.ride_queue = ride_list
        self.ride_map = {}

    def give_ride(x, y, id):
        current_ride = 0
        res = abs(x - ride_queue[0].start_pos[0]) + abs(y - ride_queue[0].start_pos[1])
        for i in xrange(len(ride_queue)):
            dist = abs(x - ride_queue[i].start_pos[0]) + abs(y - ride_queue[i].start_pos[1])
            if dist < res:
                res = dist
                current_ride = i

        # copy the ride for return
        return_ride =  deepcopy(ride_queue[current_ride])

        # remove ride from list
        del ride_queue[current_ride]
        return return_ride

    def ride_empty():
        if not ride_queue:
            return false
