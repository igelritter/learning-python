#fun with print, mainly how to format output
print "\tLet's practice everything.\n"
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'
poem="""
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print "--------------"
print poem
print "--------------"
five=10-2+3-6
print "\nThis should be five: %s" %five
#functions defined
def secret_formula(started):
    jelly_beans=started*500    
    jars=jelly_beans/1000
    crates=jars/100
    return jelly_beans,jars,crates
# This raw_input didn't originally work because it was storing the number
# entered as a string instead of an integer. I fixed that wagon!
start_point=int(raw_input("\tProvide a starting point: "))
#start_point=10000
beans,jars,crates=secret_formula(start_point)
print "\nWith a starting point of: %d" %start_point
print "We'd have %d beans, %d jars, and %d crates." %(beans,jars,crates)
start_point=start_point/10
print "\nWe can also do that this way:\n"
print "We'd have %d beans, %d jars, and %d crates." %secret_formula(start_point)
