#-------------------------------------------------------------------------------
# First class exercice - Learn Python 3 the hard way - page 188
# Author    : Benoit Stef
# Date      : 26.02.2019
#-------------------------------------------------------------------------------
import random
from urllib.request import urlopen
import sys
#get the url
WORD_URL = "https://learncodethehardway.org/words.txt"
#create an empty list
WORDS = []
#create a dictionary
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** taht takes self and @@@ params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#do they want ti drill phrases First
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#load up the words from the website and add to them to the list WORDS
for word in urlopen(WORD_URL).readlines():
    WORDS.append(str(word.strip(), encoding="utf-8"))

def convert(snippet, phrase):
    classNames = [w.capitalize() for w in random.sample(WORDS,snippet.count("%%%"))]
    otherNames = random.sample(WORDS,snippet.count("***"))
    results = []
    paramNames = []

    for i in range(0, snippet.count("@@@")):
        paramCount = random.randint(1,3)
        paramNames.append(', '.join(random.sample(WORDS, paramCount)))

    for sentence in snippet, phrase:
        result = sentence[:]

        #fake class Names
        for word in classNames:
            result = result.replace("%%%", word, 1)

        #fake other names
        for word in otherNames:
            result = result.replace("***", word, 1)

        #fake parameter lists
        for word in paramNames:
            result = result.replace("@@@", word, 1)

        results.append(result)

    return results

#keep going until they hit CTRL-D
try:
    while True:
        snippets = list(PHRASES.keys())
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

            print(question)
            input('> ')
            print("ASNWER: {}".format(answer))
except EOFError:
    print("\nBye")
