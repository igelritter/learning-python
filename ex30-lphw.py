#Initial variable setup
people = 30
cars = 30
buses = 30

#first block of comparison between cars and people
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "we can't decide."


#next comparison between just buses and cars. 
if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."


#now between people and buses    
if people > buses:
    print "Alright, let's just take the buses."
else:
    print "Fine, let's stay home then."
    
