#-------------------------------------------------------------------------------
# Functions & Files - Learn Python 3 the hard way - page 100
# Author    : Benoit Stef
# Date      : 22.02.2019
#-------------------------------------------------------------------------------
from sys import argv
script, inputFile = argv

def print_all(f):#definition of the function print all with a file as arg
    print(f.read())#print the full file to cmd

def rewind(f):#define func rewind with fil as arg
    f.seek(0)#go to start of file

def print_a_line(line_count, f):#define print line func, line num & file args
    print(line_count,f.readline())#read line from file and print to cmd

currentFile = open(inputFile)#give the file content to variable

print("First let's print the whole file \n")#print txt to cmd
print_all(currentFile)#call print all func and give teh variable to it
print("Now let's rewind, kind of like a tape")#print text
rewind(currentFile)#
print("Let's print three lines:")#

currentLine = 1
print_a_line(currentLine, currentFile)
currentLine += 1
print_a_line(currentLine, currentFile)
currentLine += 1
print_a_line(currentLine, currentFile)
