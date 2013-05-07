#An example of a recursive solution, here's the function
def simpleExp(b,n):
    if n == 0:
        return 1
    else:
        print b * simpleExp(b,n-1)
        return b * simpleExp(b,n-1)

#Here's some code to interact with the fucntion
#This doesn't really work as expected. 
base = int(raw_input("Let's see if this works. Give me a base: "))
pwr=int(raw_input("Now give me a power: "))
simpleExp(base,pwr)


