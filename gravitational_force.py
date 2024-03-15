import stdio
import sys

#accepts m1, m2, and r as command-line arguments
m1 = float(sys.argv[1])

m2 = float(sys.argv[2])

r = float(sys.argv[3])

#G is a gravitational constant
G = 6.674 * (10**-11)

#formula for gravitational force acting between the objects
f = G * ((m1*m2) / r**2)

#prints out value of f, gravitational force
stdio.writeln(f)
