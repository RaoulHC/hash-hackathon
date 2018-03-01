from ride import Ride
from car import Car

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
        for line in lines[1:]:
            nums = [int(s) for s in line.split(' ')]

            start_x,start_y = nums[0],nums[1]
            end_x,end_y = nums[2],nums[3]
            earlist_start = nums[4]
            earlist_end = nums[5]

            self.rides.append(
                Ride( [start_x,start_y],
                     [end_x,end_y],
                    earlist_start,
                    earlist_end
                    )
                )

        self.cars = []
        for i in xrange(self.n_cars):
            self.cars.append(Car())
