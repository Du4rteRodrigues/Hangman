import re
import views as vw
from Models.models import hangman as hm

# Checkes the type of the word
def check_type(word):
    for element in word:
        try:
            element ==  int(element)
        except ValueError:
            return True
        return False


# Checked the length of the letters
def check_length(letter):
    if len(letter) == 1:
        return True
    return False


# Checks if the max number of fails has been reached
def check_fails(hm):
    fails = hm.n_mistakes
    if fails > 6:
        stats(hm)
    return False


# Checkes if attempt already exists
def check_misses(word, hm):
    attempts = hm.wrong_attempts
    if word in attempts:
        return True
    return False