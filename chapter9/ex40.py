#-------------------------------------------------------------------------------
# First class - Learn Python 3 the hard way - page 184
# Author    : Benoit Stef
# Date      : 25.02.2019
#-------------------------------------------------------------------------------

class Song(object):
    #method to init itself while a new object is created
    def __init__(self, lyrics):
        self.lyrics = lyrics
    #method to sing
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#1st object created
happyBday = Song(["""
Happy birthday to you
I don't want to get sued
So I'll stop right there
"""])
#2nd object created
bullsOnParade = Song(["""
They rally around tha family
with pockets full of shells
"""])

#call the method to display for object happyBday
happyBday.sing_me_a_song()

bullsOnParade.sing_me_a_song()
