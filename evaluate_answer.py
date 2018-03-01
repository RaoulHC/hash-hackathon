from simulation_manager import SimulationManager

input_man = SimulationManager('in/a_example.in')

for ride in input_man.rides:
    print "RIDE FROM ", ride.start_pos, " TO ", ride.end_pos


# Run the simulation
for t in xrange(input_man.T):
    for car in input_man.cars:
        car.step()

