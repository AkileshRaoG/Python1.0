the_count = [1, 2, 3, 4, 5]
letters = ['a', 'b', 'c', 'd', 'e']
mix = [1, 'one', 2, 'two', 3, 'three']

for number in the_count:
    print "This is count %d" % number

for letter in letters:
    print "A letter of type %s" % letter

for i in mix:
    print "%r" % i

elements = []
for i in range(0,6):
    print "Adding %d to the list" % i
    elements.append(i)

for i in elements:
    print "Element was : %d" % i
