from sys import argv
script,filename=argv
txt=open(filename)
print "here's your file %r:" %filename
print txt.read()



##print "I'll also ask you to type it again:"
##file_again=raw_input(">")
##txt_again=open(file_again)
##print txt_again.read()
##txt_again=raw_input("Now, lets' add some text to the end of the file:  ")
##txt_again.write(file_again)
##print "Is your new text there\n"
##print txt_again.read()

