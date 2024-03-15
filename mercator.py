import math
import stdio
import sys

#accept latitude float as command-line arguemnet
lat = float(sys.argv[1])

#accept longitude float as command-line arguement
long = float(sys.argv[2])

#convert degrees into radians
lat = math.radians(lat)

#equation that computes y (lat)
#using math.log() for natural log
lat = math.log((1 + (math.sin(lat))) / (1 - (math.sin(lat)))) / 2

#writes values of 'x'(long) and 'y'(lat), with space seperation
stdio.writeln(str(long) + " " + str(lat))
