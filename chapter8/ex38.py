#-------------------------------------------------------------------------------
# Doing Things to Lists - Learn Python 3 the hard way - page 168
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
tenThings = "Apples Oranges Crows Telephone Light Sugar"
#print(tenThings)
print("wait there are not 10 things in that list. Let's fix that.")
#very powerful tool, split strings when spaced and place them to a list with ' '
stuff = tenThings.split()
print(stuff)
moreStuff = ["Day", "Night", "Song", "Frisbee",
             "Corn", "Banana", "Girl", "Boy"]

while len(stuff) !=10:
    #pop take the last element within a list and reduce the list
    nextOne = moreStuff.pop()
    print("Adding: ", nextOne)
    #extend the item that was popped from previous list to the new list
    stuff.append(nextOne)
    print("There are {} items now".format(len(stuff)))

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1]) #whoa! Fancy
print(stuff.pop())
print(' '.join(stuff)) #what? cool!
print('#'.join(stuff[3:6])) #super stellar!
