from car import Car
from queue import RideQueue
from ride import Ride

rq = RideQueue([])
c = Car()
c.step

# initialised no ride queue
print c.pos
print c.ride

# lets try some basic ride queue with one thing
r1 = Ride((1, 1), (2, 2), 0, 10, 1)
rq = RideQueue(r1)

c.initialise_ride_queue(rq)
print c.get_ride_queue()

# hack a ride onto it for now

print "Car stuff"
print "position: ", c.pos
print "ride: ", c.ride
print "riding: ", c.riding
print "time remaining: ", c.time_remaining
print

c.step()

print "Car stuff"
print "position: ", c.pos
print "ride: ", c.riding
print "time remaining: ", c.time_remaining

