import stdio
import sys

#Accept command line argument
n = int(sys.argv[1])

#Set nogard and dragon to string F 
dragon = "F"
nogard = "F"

#repeat for i from 1 to n itself
for i in range(1, n+1):
#exchange dragon and no gaurd with dragon "L" nogard and dragon "R" nogard
    temp = dragon 
    dragon = dragon + "L" + nogard
    nogard = temp + "R" + nogard  

#exchange L with R and R with L    


#write dragon  
stdio.writeln(dragon)

    

        