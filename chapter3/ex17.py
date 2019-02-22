#-------------------------------------------------------------------------------
# More Files - Learn Python 3 the hard way - page 88
# Author    : Benoit Stef
# Date      : 22.02.2019
#-------------------------------------------------------------------------------
from sys import argv
#new feature here we import command named exist that is True if a file exists
from os.path import exists

script, fromFile, toFile = argv

print("Copying from", fromFile, "to", toFile)

#we could do these on on line, how?
inData=open(fromFile).read()
print("The input file is", len(inData),"bytes long")
print("Rdy, hit RETURN to continue, CTRL-C to abort")

outFile= open(toFile,'w')
outFile.write(inData)

print("Alright, all done.")
outFile.close()
