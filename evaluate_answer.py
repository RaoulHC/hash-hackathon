from simulation_manager import SimulationManager
from car import Car

in_file = 'in/a_example.in'
simulation = SimulationManager(in_file)

for ride in simulation.rides:
    print "RIDE ", ride.id, ": ", ride.start_pos, " TO ", ride.end_pos


# Run the simulation
for t in xrange(simulation.T):
    Car.time = t
    for car in simulation.cars:
        car.step()

    # Have we finished ?
    if simulation.ride_queue.ride_empty():
        break

simulation.save_answer(in_file.replace('in', 'out'))
