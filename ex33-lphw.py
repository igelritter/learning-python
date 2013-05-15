#This was originally an intro to while loops
#For extra credit, you change the loop into a function and then
#call it
##def f(x, y):
##    """This is a silly thing that shows you the effects of a while loop
##    by taking a variable from the user and then cranking through the loop"""
##    i = 0
##    numbers = []
##    while i < x:
##        print "At the top i is %d" %i
##        numbers.append(i)
##        i += y
##        print "Numbers now: " ,numbers
##        print "At the bottom i is %d\n" %i
##    print "The numbers:"
##    for num in numbers:
##        print num
#This is the same thing but with a for loop. Notice how cleaner it is. Two
#lines less of code, and no 'i' state variable. You do lose the functionality
#of defining how much you want the loop to increment by.
def f(x):
    """This is a silly thing that shows you the effects of a while loop
    by taking a variable from the user and then cranking through the loop"""
    numbers = []
    for i in range(0, x):
        print "At the top i is %d" %i
        numbers.append(i)
        print "Numbers now: " ,numbers
        print "At the bottom i is %d\n" %i
    print "The numbers:"
    for num in numbers:
        print num
#we are taking input from the user and then calling the function
x = int(raw_input("Give me a number: "))
#y = int(raw_input("How much would you like to increment by? "))
f(x)
