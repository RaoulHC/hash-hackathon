from car import Car
from queue import RideQueue
from ride import Ride

rq = RideQueue([])
c = Car()
c.step

print c.pos
print c.ride

# lets try some basic ride queue with one thing

r1 = Ride((1, 1), (2, 2), 0, 10, 1)
rq = RideQueue(r1)

print r1
c.initialise_ride_queue([])
print c.get_ride_queue()

# hack a ride onto it for now
c.ride = r1

print "Car stuff"
print "position: ", c.pos
print "ride: ", c.ride
print "riding: ", c.riding
print "time remaining: ", c.time_remaining
print

c.ride_step()

print "Car stuff"
print "position: ", c.pos
print "ride: ", c.riding
print "time remaining: ", c.time_remaining

