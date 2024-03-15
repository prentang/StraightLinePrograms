import stdio
import sys

n = int(sys.argv[1])

#set a, b to 1 and i to 3. 
#a, b are the first two numbers to the set
a = 1 
b = 1 
i = 3 


#repeat as long as i <= n; exchange a and b with b and a + b
#make temp hold value 
#increment i by one 
while i <= n:
    temp = a 
    a = b 
    b = temp + b  
    i += 1 

#write the nth fibonacci number
stdio.writeln(b)