import stdio
import sys

#accepts x,y,z (as int) as command-line arguments 
x = int(sys.argv[1])
y = int(sys.argv[2])
z = int(sys.argv[3])

#takes variables and finds the min and max
alpha = min(x,y,z)
omega = max(x,y,z)

#gets rid of min and max from input, gets middle number
mid = z + x + y - alpha - omega

#writes out smallest to largest with spaces inbetween
stdio.writeln(str(alpha) + " " + str(mid) + " " + str(omega))

