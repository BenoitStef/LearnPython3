#-------------------------------------------------------------------------------
# While loops - Learn Python 3 the hard way - page 150
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
i = 0
numbers = []
while i < 6:
     print("At the top i is {}".format(i))
     numbers.append(i)

     i+=1
     print("Numbers now:", numbers)
     print("At the bottom i is {}".format(i))

print("The numbers: ")

for num in numbers:
    print(num)
