states = {
    'Karnataka':'KA',
    'Kerala':'KL',
    'Tamil Nadu':'TN',
    'Maharashtra':'MH',
    'Andhra Pradesh':'AP'
}

cities = {
    'KA':'Bangalore',
    'TN':'Chennai',
    'MH':'Pune'
}

cities['AP']='Warangal'
cities['KL']='Cochin'

print '-' * 10
print "KA state has: ", cities['KA']
print "TN state has: ", cities['TN']

print '-' * 10
print "AP state has: ", cities[states['Andhra Pradesh']]
print "MH state has: ", cities[states['Maharashtra']]

for state, abbrev in states.items():
    print "%s is abbreviated as %s " % (state, abbrev)

print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s " % (abbrev, city)

print '-' * 10
for state, abbrev in states.items():
    "%s is abbreviated as %s and has the city %s" % (state, abbrev, cities[abbrev])

print '-' * 10
state = states.get('Udupi')

if not state:
    print "Sorry, no Udupi"

city = cities.get('UD', 'Does not exist')
print "The city for the state 'UD' is : %s" % city
