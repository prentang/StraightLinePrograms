import math
import stdio
import sys

#accept two floats: avg and t(time)
avg = float(sys.argv[1])
t = float(sys.argv[2])

#equation for probability, computes and writes out p
#math.exp for e^x
p = math.exp(-(t*avg))

#writes proability to standard output
stdio.writeln(p)
