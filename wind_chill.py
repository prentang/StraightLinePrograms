import stdio
import sys

#temperature (in Fahrenheit), accepts t as a command line argument
t = float(sys.argv[1])

#wind speed (in MPH), accepts v as a command line argument
v = float(sys.argv[2])

#windchill formula, computes windchill 
w = 35.74 + (0.6215 * t) + ((0.4275*t) - 35.75) * v**0.16

#prints out value windchill
stdio.writeln(w)



