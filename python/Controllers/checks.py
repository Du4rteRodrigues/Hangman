import re
import views as vw
from Models.models import hangman as hm
from Controllers.progress import stats
from Controllers.attempts import *

# Checkes the type of the word
def check_type(word):
    for element in word:
        try:
            element ==  int(element)
        except ValueError:
            return True
        return False


def check_letter(letter,hm,md):
    if not try_letter(letter,hm,md):
        hm.n_mistakes +=1
        hm.n_rounds +=1
        return False
    hm.n_rounds +=1
    return hm


def check_word(word,hm,md):
    if not try_word(word,hm,md):
        hm.n_mistakes +=2
        hm.n_rounds +=1
        return False
    hm.n_rounds +=1
    return hm


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