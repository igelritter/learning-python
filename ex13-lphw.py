from sys import argv
script,first,second,third=argv
print "The script is called:" ,script
print "Your first variable is:" ,first
print "Your second variable is:" ,second
print "Your third variable is:" ,third
print """
And now that we've looked at your CLI
arguments. Let's take some additional
data and spit it back in your face!
"""
prompt1=raw_input("\tGive it to me?")
prompt2=raw_input("\t about another?")
print "\nHere was your second argument from the command line"
print "followed with your second string from standard in\n"
print "%s and %s in your face!"%(first,prompt2)
