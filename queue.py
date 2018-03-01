# queue class file

class queue(object, ride_list, car_list):

    def __init__(self):
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
        return ride_queue[current_ride]


is ride empty

    def output


    def step(self):
        if ride_queue == []:
            self.finish = True
