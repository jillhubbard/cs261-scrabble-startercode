# CS261 Scrabble
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
WORDLIST_FILENAME = "words.txt"

# You do not need to modify this function. It is provided for you.
def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def play_game(word_list):

    """
    Print welcome message
    Deal a hand
    While the hand is not empty
        Display the hand
        Ask the user to enter a word or !! to indicate that you are finished
        If they entered !! break out of the loop
        Calculate the score for the word the user entered 
        Print word and the points earned
        Update the hand by removing the letters in the word
    Print total score for the hand
    """
    pass  # TO DO... Remove this line when you implement this function

#
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
