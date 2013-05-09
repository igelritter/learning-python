from math import *

targ = int(raw_input("How many primes do you want to find?: "))

#initiating state variables
#the program assumes that 1 and 2 are prime and starts counting at 2

foundp = 3
can = 5

#entering a while loop that exits when found primes is no longer less than target

while foundp < targ:
    #print "Entering loop\n"
    prime = True
#for loop that tests all number up to the target number for divisibility

    
    for x in range(3,can-1):
        #print " \n\t%r modulo %r"%(can,x)
        if can%x == 0:
            prime = False
            break 
        
    if prime == True:
        print "\n%r is a prime number" %can
        foundp = foundp+1

        
    can = can+2
