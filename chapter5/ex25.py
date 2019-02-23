# Even more practice - Learn Python 3 the hard way - page 122
# Author    : Benoit Stef
# Date      : 23.02.2019
#-------------------------------------------------------------------------------
def break_words_func(stuff):
    """This function will break up words for us. """
    words = stuff.split(' ')#this split character with a space in between
    return words

def sort_words_func(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word_func(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word_func(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence_func(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words_func(sentence)
    return sort_words_func(words)

def print_first_and_last_func(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words_func(sentence)
    print_first_word_func(words)
    print_last_word_func(words)

def print_first_and_last_sorted_func(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence_func(sentence)
    print_first_word_func(words)
    print_last_word_func(words)
