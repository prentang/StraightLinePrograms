import stdio
import sys

#n1,n2 are command line integers  command-line arguments 
#p is command line float command-line argument
n1 = int(sys.argv[1])
n2 = int(sys.argv[2])
p = float(sys.argv[3])

#probability 
q = 1 - p 

#probability equation 1
p1 = (1 - ((p/q)**n2)) / (1 - ((p/q)**(n1+n2)))

#probability equation 2 
p2 = (1 - ((q/p)**n1)) / (1 - ((q/p)**(n1+n2)))

#have to make sure cast float to str
#write probability of p1 AND p2
stdio.writeln(str(p1) + " " + str(p2))

