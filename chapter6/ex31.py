#-------------------------------------------------------------------------------
# Making decisions - Learn Python 3 the hard way - page 138
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
print("""You enter a dark room with two doors.value
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("""There's a gient bear eating a cheese cake.
    what do you do?
    1. Take the cake.
    2. Scream at the bear.
    """)

    bear = input('> ')

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The ebar eats your legs off. Good job!")
    else:
        print("Well, doing {} is probably better".format(bear))

elif door == "2":
    print("""You stare into the endless abyss at Cthulhu's retinaself.
    1. Blueberriesself.
    2. Yellow jacket clothepsins.
    3. Understanding revolvers yelling melodies.
    """)

    insanity = input('> ')

    if insanity == "1" or insanity == "2":
        print("You body survives powered by a mind of jello.\nGood job!")
    else:
        print("The insanity rots your eyes into a pool of muck.\nGood job!")
else:
    print("You stumble around and fall on a knife and die. Good job!")
