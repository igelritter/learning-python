def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print "You have %d cheeses!" %cheese_count
    print "You have %d boxes of crackers!" %boxes_of_crackers
    print "Man, that's enough for a party!"
    print "Get a blanket.\n"
print"\tWe can just give the function numbers directly:\n"
cheese_and_crackers(20,30)
print "\tOR, we can use variables from our script:\n"
amount_of_cheese=10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)
print "\twe can even do math inside too:\n"
cheese_and_crackers(10+20,5+6)
print "\tAnd we can combine the two, variables and math:\n"
cheese_and_crackers(amount_of_cheese+100,amount_of_crackers+1000)
