import math
import stdio
import sys

#accepts theta 1(float), n1(float), and n2(float) as command-line arguments
theta1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])

#converts theta 1(float), n1(float), and n2(float) to radians
theta1 = math.radians(theta1)
n1 = math.radians(n1)
n2 = math.radians(n2)

#computes theta 2
#use math.asin for arcsine
theta2 = math.asin((n2/n1 * 1 / math.sin(theta1)) ** -1)

#converts output to degrees and writes
stdio.writeln(math.degrees(theta2))


