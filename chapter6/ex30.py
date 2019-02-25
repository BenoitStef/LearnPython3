#-------------------------------------------------------------------------------
# if/elif/else - Learn Python 3 the hard way - page 138
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
people = 30
cars = 40
trucks = 15

if cars > people:
    print("we should take the cars.")
elif cars < people:
    print("we chould not take the cars")
else:
    print("we can't decide")

if trucks > cars:
    print("That's too many truck")
elif trucks < cars:
    print("maybe we could take the trucks")
else:
    print("we still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
