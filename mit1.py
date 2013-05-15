from math import *

targ = int(raw_input("How many primes do you want to find?: "))

#initiating state variables
#the program assumes that 1, 2, and 3 are prime and starts counting at 3

foundp = 3
can = 5

#entering a while loop that exits when found primes is no longer less than target

while foundp < targ:
    #print "Entering loop\n"
    prime = True
#for loop that tests all number up to the target number for divisibility
#There's a possibility here to make the code more effeicent by eliminating
#a lot of search space by stopping the search at the square of 'can' instead
#of going all the way up to 'can'
    
    for x in range(3,can-1):
        #print " \n\t%r modulo %r"%(can,x)
        if can%x == 0:
            prime = False
            break 
#When a prime is found the following conditional increases found primes by one        
    if prime == True:
        print "\n%r is a prime number" %can
        foundp = foundp+1

#after exiting the for loop, the candidate is augmented by +2. This means that the candidate numbers
#are always odd. This allows use to eliminate all even numbers.
    can = can+2
