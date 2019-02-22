#-------------------------------------------------------------------------------
# Reading & writing files - Learn Python 3 the Hard way - page 84
# Author: Benoît Stef
# Date: 22.02.2019
#
# close - Closes the file. Like File->Save.. in your editor
# read - Reads the content of the file. You can assign the result to a variable
# readline - Reads just one line of a text file
# truncate - Empties the file. Watch out if you care about the file
# write('stuff') - Writes "stuff" to the file
# seek(0) - Move the read/write location to the beginning of the file
#-------------------------------------------------------------------------------
from sys import argv

script, filename = argv

print("We are going to erase", filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")
print("Opening the file...")
#open file in write mode and pass it in var target
target = open(filename, 'w')
#this erase the file
print("Truncating the file. Goodbye")
target.truncate()

print("Now I'm going to ask you  for 3 lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm goint to write these to the file.")
#write to file
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
#close file
print("and finally, we close it")
target.close()
