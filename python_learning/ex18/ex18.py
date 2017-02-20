from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file: \n"

print_all(current_file)

print "Let's rewind."
rewind(current_file)
print

print "Let's print 3 lines: "

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers

cheese_and_crackers(20, 30)

amount_of_cheese = 10
amount_of_crackers=50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

def print_two(*args):
    arg1, arg2 = args
    print "agr1: %r, arg2: %r" % (arg1, arg2)

def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: %r" % arg1

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
