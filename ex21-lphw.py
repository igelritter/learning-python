#functions are defined in this block
def add(a,b):
    print "Adding %d + %d" %(a,b)
    return a+b
def subtract(a,b):
    print "Subtracting %d - %d" %(a,b)
    return a-b
def multiply(a,b):
    print "Multiplying %d * %d" %(a,b)
    return a*b
def divide(a,b):
    print "Dividing %d / %d" %(a,b)
    return a/b
#main block of code
print "\tLet's do some math with just functions!"
age=add(30,5)
height=subtract(78,4)
weight=multiply(90,2)
iq=divide(100,2)
print "\tAge: %d, Hieght: %d, Weight: %d, IQ: %d\n" %(age,height,weight,iq)
#A puzzle for the extra credit, type it in anyway.
print "\tHere is a puzzle.\n"
what=add(age,subtract(height,multiply(weight,divide(iq,2))))
print "\nThat becomes: " ,what,"\nCan you do it by hand?"
