#-------------------------------------------------------------------------------
# Prompting & passing - Learn Python 3 the Hard way - page 76
#-------------------------------------------------------------------------------
from sys import argv

script, userName = argv
prompt = '> '

print("Hi ",userName,"I'm the", script,"script")
print("I'd like to ask you a few questions")
print("Do you like me", userName,"?")
likes = input(prompt)

print("Where do you live",userName," ?")
lives = input(prompt)

print("""
Alright, so you said""", likes ,"""about liking myself.
You live in""", lives, """Not sure where that is.
""")
