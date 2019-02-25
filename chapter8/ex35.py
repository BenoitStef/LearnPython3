#-------------------------------------------------------------------------------
# Accesing Elements of lists - Learn Python 3 the hard way - page 156
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------
from sys import exit

#func definition
def gold_room_func():
    print("This room is full of gold. How much do you take?")

    choice = input('> ')
    if "0" in choice or "1" in choice:
        howMuch= int(choice)
    else:
        dead_func("Man, learn to type a number.")

    if howMuch < 50:
        print("nice, you're not greedy, you win!")
        exit(0)
    else:
        dead_func("You greedy bastard!")

def bear_room_func():
    print("""There is a bear here.
     The bear has a bunch of honey.
     The fat bear is in front of another door.
     How are you going to move the bear?
    """)
    bearMoved = False

    while True:
        choice = input('> ')

        if choice == "take honey":
                dead_func("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bearMoved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bearMoved = True
        elif choice =="taunt bear" and bearMoved:
            dead_func("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bearMoved:
            gold_room_func()
        else:
            print("I got no idea what that means.")

def cthulhu_room_func():
    print("""Here you see the great evil Cthulhu.
    He, it. whatever stares at you and you go insaneself.
    Do you flee for your life ir eat your head?
    """)

    choice = input('> ')

    if "flee"in choice:
        start_func()
    elif "head" in choice:
        dead_func("well that was tasty!")
    else:
        cthulhu_room_func()

def dead_func(why):
    print(why, "Good Job!")
    exit(0)

def start_func():
    print("""You are in a dark room.
    There is a door to your right and left.
    Which one do you take?
    """)

    choice = input('> ')

    if choice == "left":
        bear_room_func()
    elif choice == "right":
        cthulhu_room_func()
    else:
        dead_func("You stumble around the room until you starve")

start_func()
