import stdio
import sys


#accept p and q as command line arguments
p = int(sys.argv[1])

q = int(sys.argv[2])


# while p mod q is not equal to 0, remainder not equal to zero, if divides evenly exit loop
while p%q != 0:
  
  #exchange p and q with q and p mod q.
    temp = p 
    p = q       
    q = temp % q 


#write gcd (q)
stdio.writeln(q)
