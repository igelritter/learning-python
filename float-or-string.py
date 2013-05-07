##This code shows you the difference between types with default raw_input
##
##y = raw_input('enter a number:')
##print type(y)
##print y
##y = float(raw_input('Enter a number:   '))
##print type(y)
##print y
##y = int(raw_input('Enter yet another number:   '))
##print type(y)
##print y
##
##This code shows a simple if/else conditional
##
##x = int(raw_input('Enter an integer:   '))
##if x%2 == 0:
##     print 'Even'
##else:
##     print 'Odd'
##     if x%3 != 0:
##          print 'And not divisible by 3'
##
##
##Find the cube root of a perfect cube
##x = int(raw_input('Enter an integer:   '))
##ans = 0
##print "absolute value of x = %d" %(abs(x))
##while ans*ans*ans < abs(x):
##    ans = ans + 1
##    print 'current guess =', ans
##if ans*ans*ans !=abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of ' + str(x) ' is ' + str(ans)
##    ## another way to do the same print statement
##    ## print 'Cube root of %s is %s' %(str(x),str(ans))
##
##
##x = int(raw_input('Enter an integer:   '))
##for ans in range(0, abs(x)+1):
##    if ans**3 == abs(x):
##        break
##if ans**3 != abs(x):
##    print x, 'is not a perfect cube'
##else:
##    if x < 0:
##        ans = -ans
##    print 'Cube root of %s is %s' %(str(x),str(ans))
##

##Here is an example of finding square roots with bisection search
##x = float(raw_input('Enter a number:   '))
##epsilon = 0.01
##numGuesses = 0
##low = 0.0
##high = x
##ans = (high + low)/2.0
##while abs(ans**2 -x) >= epsilon and ans <=x:
##    print low, high, ans
##    numGuesses += 1
##    if ans **2 < x:
##        low = ans
##    else:
##        high = ans
##    ans = (high + low)/2.0
##print 'numGuesses = %d' %(numGuesses)
##print "%s is close to the square root of %s" %(str(ans),str(x))

def withinEpsilon(x, y, epsilon):
    """x,y,epsilon floats. epsilon > 0.0
       returns True if x is within epislon of y"""
    return abs(x - y) <= epsilon





