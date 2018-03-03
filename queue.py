from copy import deepcopy
from car import Car


class RideQueue(object):
    """

    """
    def __init__(self, ride_list, bonus):
        """
        """
        self.ride_queue = ride_list
        self.original_ride_list = deepcopy(ride_list)

        self.ride_map = {}
        self.bonus = bonus
        self.missed_rides = 0

    def distance(self, ride, x,y):
        manhat_dist = abs(x - ride.start_pos[0]) + abs(y - ride.start_pos[1])
        # the time a car will wait can be added to the distance between a car
        # and a ride as it can be thought of as an effective additional distance
        wait_distance = max(0,ride.earliest_step - Car.time - manhat_dist)

        score_for_ride = 0

        if Car.time + wait_distance + ride.length() <= ride.latest_step:
            score_for_ride += ride.length()
            if ride.earliest_step - Car.time - manhat_dist <= 0:
                score_for_ride += self.bonus

        # Prioritize car
        return manhat_dist + wait_distance, score_for_ride

    def give_ride(self, x, y, car_id):
        """
        Give a car located at x,y the closest ride to it
        """

        # Delete expired rides -
        for x in sorted(xrange(len(self.ride_queue)), reverse=True):
            if self.ride_queue[x].latest_step < Car.time:
                self.missed_rides += 1
                del self.ride_queue[x]

        # Start with the first ride in the queue as a trial solution.
        best_distance, best_score_for_ride = self.distance(self.ride_queue[0],
                                                           x,
                                                           y)
        current_ride = 0

        #
        for i in xrange(len(self.ride_queue)):
            # for each ride evaluate the distance between the car and the ride
            distance_to_car, score_for_ride = self.distance(self.ride_queue[i],x,y)

            # Go to the car ride that can be started the soonest
            # If the evaluate ride will be started at the same time
            # as the best so far, chose whichever gives us more points
            if distance_to_car < best_distance:
            # if (distance_to_car < best_distance) or (
            #     distance_to_car == best_distance and
            #     score_for_ride > best_score_for_ride
            #    ):
                best_distance = distance_to_car
                best_score_for_ride = score_for_ride
                current_ride = i

        # Skip rides that we cannot finish - it's better to leave the
        # car free for other rides, and that ride in the runnings for
        # other closer cars
        if best_score_for_ride == 0:
            return None

        # Store the assigned ride's id to the final list
        if car_id in self.ride_map:
            self.ride_map[car_id].append(self.ride_queue[current_ride].id)
        else:
            self.ride_map[car_id] = []
            self.ride_map[car_id].append(self.ride_queue[current_ride].id)

        # copy the ride for return
        return_ride = deepcopy(self.ride_queue[current_ride])

        # remove ride from list
        del self.ride_queue[current_ride]
        return return_ride

    def ride_empty(self):
        return len(self.ride_queue) == 0
