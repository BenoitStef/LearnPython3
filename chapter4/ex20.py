#-------------------------------------------------------------------------------
# Functions & Files - Learn Python 3 the hard way - page 100
# Author    : Benoit Stef
# Date      : 22.02.2019
#-------------------------------------------------------------------------------
from sys import argv
script, inputFile = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count,f.readline())

currentFile = open(inputFile)

print("First let's print the whole file \n")
print_all(currentFile)
print("Now let's rewind, kind of like a tape")
rewind(currentFile)
print("Let's print three lines:")

currentLine = 1
print_a_line(currentLine, currentFile)
currentLine += 1
print_a_line(currentLine, currentFile)
currentLine += 1
print_a_line(currentLine, currentFile)
