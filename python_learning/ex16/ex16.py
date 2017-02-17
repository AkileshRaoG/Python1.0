from sys import argv
script, filename = argv

print "We're going to erase %r" % filename

raw_input("?")

print "Opening the file ...."
target = open(filename, 'w')

print "Truncating the file."
target.truncate()

print "I'm going to write these to the file."

line1= raw_input("line 1: ")
line2= raw_input("line 2: ")
line3= raw_input("line 3: ")

print "I'm going to write these to the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Closing file")
target.close()
