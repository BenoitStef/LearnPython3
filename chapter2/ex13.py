#-------------------------------------------------------------------------------
# Parameter Unpacking Variables - Learn Python 3 the Hard way - page 72
#-------------------------------------------------------------------------------
#import module argv from sys -> add new feature to code
from sys import argv
#read the WYSS section for how to run this, here we unpack what's in argv
# argv is the argument that you have give when you call the script
script, first, second, third = argv

print("The script is called:", script)
print("Your first var is:", first)
print("Your second var is:", second)
print("Your third var is:", third)
