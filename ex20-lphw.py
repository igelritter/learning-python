from sys import argv
script,input_file=argv
#functions defined in this block
def print_all(f):
    print f.read()
def rewind(f):
    f.seek(0)
def print_a_line(line_count,f):
    print line_count,f.readline()
#body of the script follows:
current_file=open(input_file)
print "\tFirst, let's print the whole file:\n"
print_all(current_file)
print "\tNow, let's rewind, kind of like a tape.\n"
rewind(current_file)
print "\tLet's print three lines:\n"
current_line=1
#Look! I cheated and just did a for loop. I am full of wisdom!
#The author wanted to perform the same action three times. 
for x in range(1,4):
    print_a_line(current_line,current_file)
    current_line=current_line+1
