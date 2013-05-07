target = int(50)
foundp = int(7)
can = int(14)

while foundp < abs(target):
     if can%2 == 0:
        can = can+1
     if can%3 == 0:
        can = can+1
     if can%5 == 0:
        can = can+1
     if can%7 == 0:
        can = can+1
     if can%13 == 0:
        can = can+1
else:
        print "Found one: %d" %(can)
        can = can+1
        foundp = foundp+1
    
