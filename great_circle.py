import math
import stdio
import sys

#accepts x1,y1,x2,y2 as float command-line arguments
x1 = float(sys.argv[1])
y1 = float(sys.argv[2])

x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

#convert degrees to radians
x1 = math.radians(x1)
y1 = math.radians(y1)

x2 = math.radians(x2)
y2 = math.radians(y2)

#computes great circle distance d, calculating arccosine of a number
d = 6359.83 * math.acos((math.sin(x1) * math.sin(x2)) + (math.cos(x1) * math.cos(x2) * math.cos((y1-y2))))


#write out the value of great circle distance, 'd'
stdio.writeln(d)

