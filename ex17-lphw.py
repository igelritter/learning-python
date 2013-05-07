from sys import argv
from os.path import exists
script,from_file,to_file=argv
print "Copying from %r to %r" %(from_file,to_file)
#we could do these two on one line too, how?
#indata=input.read(open(from_file))
input=open(from_file)
indata=input.read()
print "The input file is %d bytes long" %len(indata)
print "Does the output file exist? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input('>')
output=open(to_file,'w')
#notice that this command is overwriting whatever is in the target file
#if you wanted to add to the target file you would need append, like this
# output=open(to_file,'a')
output.write(indata)
print "Alright, all done."
output.close()
input.close()
