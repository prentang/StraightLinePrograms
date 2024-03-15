import stdio
import sys

#Accept m,d,y (int) as command line arguements 
m = int(sys.argv[1])
d = int(sys.argv[2])
y = int(sys.argv[3])

#Compute equation, solve for Y
Yfin =  y - (14 - m) // 12

#Compute equation, solve for X
Xfin = Yfin + (Yfin // 4) - (Yfin // 100) + (Yfin // 400)

#Compute equation, solve for M
Mfin = m + 12 * ((14 - m)//12) - 2 

#Compute equation to obtain dow.
dow = (d + Xfin + 31 * Mfin // 12) % 7 

day = str(dow)

#Set output to the appropriate string based on value.
if dow == 0:
    day = "Sunday"
elif dow == 1:
    day = "Monday"
elif dow == 2:
    day = "Tuesday"
elif dow == 3:
    day = "Wednesday"
elif dow == 4:
    day = "Thursday"
elif dow == 5:
    day = "Friday"
elif dow == 6:
    day = "Saturday"
else: 
    stdio.writeln("Error")

#prints out day based on value
stdio.writeln(day)