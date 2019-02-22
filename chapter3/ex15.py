#-------------------------------------------------------------------------------
# Reading files - Learn Python 3 the Hard way - page 80
# Author: Benoît Stef
# Date: 22.02.2019
#-------------------------------------------------------------------------------
#get the module to be ablle to pass arguments at first
from sys import argv
#gathering the 2 arguments in unpacking
script, fileName = argv
#open txt file in default mode
txt = open(fileName)
#print the fileName
print("Here's your file", fileName,":")
#txt.read get the thw whole string chain and we print it
print(txt.read())
txt.close()
#same but we pass the fileName as a scanf style
print("Type the filename again:")
fileAgain = input("> ")
txtAgain = open(fileAgain)
print(txtAgain.read())
txtAgain.close()
