#This is modified code from the MIT1 which explores the relationship
#between the log sum of all the primes below a number n
#and log(e**n) and how the ratio is bounded from above

#need math for log and exp functions
from math import *

targ = int(raw_input("what number do want to test?: "))

#initiating state variables
#targe is log10(e**n) This will be compared at the end with the accumulator

can = 1
acc = 0
targe = targ*log10(exp(1))

#entering a while loop that exits when found primes is no longer less than target

while can < targ:
    #print "Entering loop\n"
    prime = True
#for loop that tests all number up to the target number for divisibility
    
    for x in range(3,can-1):
        #print " \n\t%r modulo %r"%(can,x)
        if can%x == 0:
            prime = False
            break 
#found primes are then calculated log10 and feed into an accumulator variable.         
    if prime == True:
        print "\n%r is a prime number" %can
        acc = acc+log10(can)

        
    can = can+1

print "Accumlator has found the log sum of %r \nfor the sum of all the primes before %r." %(acc,targ)
print "\nThe ratio is %r" %(acc/targe)

