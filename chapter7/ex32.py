#-------------------------------------------------------------------------------
# Loop & Lists - Learn Python 3 the hard way - page 146
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
theCount = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for-loop goes through a list
for number in theCount:
    print("This is count {}".format(number))

#same as above
for fruit in fruits:
    print("a fruit of type:",fruit)

#also we can go through mixed lists too
#notice we have use to use {} since we don't know what's in it
for i in change:
    print("I got ",i)

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range (0, 6):
    print("Adding {} to the list".format(i))
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print("Elements was: {}".format(i))