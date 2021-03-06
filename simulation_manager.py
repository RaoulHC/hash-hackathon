from ride import Ride
from car import Car
from queue import RideQueue

class SimulationManager:
    def __init__(
        self,
        in_file):
        # LOAD THE INPUT
        with open(in_file,'r') as f:
            lines = f.readlines()

        # First line is R C number_of_cars, number_of_rides, bonus_for_starting_on_time and maximum Time
        nums = [int(s) for s in lines[0].split(' ')]
        self.R,self.C,self.n_cars,self.n_rides, self.bonus,self.T = nums[0],nums[1],nums[2],nums[3],nums[4], nums[5]

        print "LOADED FILE: ", in_file
        print "City size: rowsxcols = ", self.R, "x", self.C
        print "n_cars =  ", self.n_cars
        print "n_rides =  ", self.n_rides
        print "bouns for starting a ride on time =  ",self.bonus
        print "Number of stis in sim: ",self. T

        # Now read in the rides
        self.rides = []
        for r_id,line in enumerate(lines[1:]):
            nums = [int(s) for s in line.split(' ')]

            start_x,start_y = nums[0],nums[1]
            end_x,end_y = nums[2],nums[3]
            earlist_start = nums[4]
            earlist_end = nums[5]

            self.rides.append(
                Ride([start_x, start_y],
                     [end_x, end_y],
                     earlist_start,
                     earlist_end,
                     r_id
                     )
                )

        # Create the queue
        self.ride_queue = RideQueue(self.rides, self.bonus)

        #
        self.cars = []
        for i in xrange(self.n_cars):
            self.cars.append(Car())
            self.cars[-1].initialise_ride_queue( self.ride_queue)

    def save_answer(self, out_file):
        """
        Read the final
        """
        print ""
        print "Solution found"
        with open(out_file,'w') as f:
            for car_id in self.ride_queue.ride_map:
                line = str(len(self.ride_queue.ride_map[car_id]))
                for ride_id in self.ride_queue.ride_map[car_id]:
                    line += " " + str(ride_id)
                f.write(line + "\n")
                print line

    def evaluate_score(self):
        score = 0
        for car_id in self.ride_queue.ride_map:
            x,y,t = 0,0,0
            for ride_id in self.ride_queue.ride_map[car_id]:
                ride_score = 0

                # work out the time the car will arrive at the place
                d = self.ride_queue.original_ride_list[ride_id].distance2start([x,y])
                t += d
                if t <= self.ride_queue.original_ride_list[ride_id].earliest_step:
                    ride_score += self.bonus
                    t = self.ride_queue.original_ride_list[ride_id].earliest_step

                # complete the jounrey
                t += self.ride_queue.original_ride_list[ride_id].length()
                x,y = self.ride_queue.original_ride_list[ride_id].end_pos[0],self.ride_queue.original_ride_list[ride_id].end_pos[1]

                # Award points for the length of the journey if we completed it on time
                if t <= self.ride_queue.original_ride_list[ride_id].latest_step:
                    ride_score += self.ride_queue.original_ride_list[ride_id].length()
                else:
                    ride_score = 0
                # add it to total
                score += ride_score

        print "SCORE: ", score
        print "Missed Rides: ", self.ride_queue.missed_rides
        return score

