#-------------------------------------------------------------------------------
# Dictionaries! - Learn Python 3 the hard way - page 175
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
#create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

#create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

#add more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
spacer = '-' * 10
print(spacer)
print("NY State has: ", cities['NY'])

#print some states
print(spacer)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

#do it by using the states then cities dict
print(spacer)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation
print(spacer)
for state, abbrev in list(states.items()):
    print("{} is abbreviated {}".format(state, abbrev))

#print every city in states
print(spacer)
for abbrev, city in list(cities.items()):
    print("{} has the city {}".format(abbrev, city))

#now do both
print(spacer)
for state, abbrev in list(states.items()):
    print("{} state is abbreviated {} and has city {}".format(state, abbrev, cities[abbrev]))

print(spacer)
#safely get an abbreviation by state that might not be there
state = states.get('Texas')
if not state:
    print("sorry, no Texas")

#get a city with a default value
city = cities.get('TX', 'Does not exist')
print("The city for state 'TX' is: {}".format(city))
