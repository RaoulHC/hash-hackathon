from copy import deepcopy
# queue class file

class RideQueue(object):

    def __init__(self, ride_list):
        self.ride_queue = ride_list
        self.ride_map = {}

    def give_ride(x, y, car_id):
        # Iterate over
        current_ride = 0
        res = abs(x - ride_queue[0].start_pos[0]) + abs(y - ride_queue[0].start_pos[1])
        for i in xrange(len(ride_queue)):
            dist = abs(x - ride_queue[i].start_pos[0]) + abs(y - ride_queue[i].start_pos[1])
            if dist < res:
                res = dist
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
