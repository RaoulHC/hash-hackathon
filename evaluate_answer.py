from simulation_manager import SimulationManager
from car import Car

in_files = [
    'in/a_example.in',
    'in/b_should_be_easy.in',
    'in/c_no_hurry.in',
    'in/d_metropolis.in',
    'in/e_high_bonus.in'
]

for in_file in in_files:
    simulation = SimulationManager(in_file)

    print "PROCESSING FILE: ", in_file
    # Run the simulation
    for t in xrange(simulation.T):
        Car.time = t
        for car in simulation.cars:
            car.step()

        # Have we finished ?
        if simulation.ride_queue.ride_empty():
            print "THE RIDE QUEUE IS EMPTY: QUITTING!"
            break

    simulation.save_answer(in_file.replace('in', 'out'))
