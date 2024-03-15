import stdio
import stdrandom
import sys

#accept n as a command line argument
n = int(sys.argv[1])

#simulate a single roll of a n-sided die
#add two random to get sum of numbers rolled, has to have a low of 1 for each die
#exclusive of n, add + 1 to include n
sum = stdrandom.uniformInt(1, n+1) + stdrandom.uniformInt(1, n+1)


#print out sum
stdio.writeln(sum)




