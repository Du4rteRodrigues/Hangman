import re
import views as vw
from models import hangman as hm
import os

# Shows all operations
def get_operations():
    print("x: End Game")
    print("1: Try Letter")
    print("2: Try Word")
    print("3: View Word")
    print("4: View Hangman")
    print("5: View Failed Attempts")


# Saves the word 
def save_word(word,hm):
    hm.word = word
    h_word = ""
    space = "_ "
    for element in word:
        h_word += space
    hm.hidden_word = h_word
    clear_terminal()
    return True


# Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

#------------------------------------Checks------------------------------------

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

#-------------------------------------------------------------------------------------------

#---------------------------------------User_attempts---------------------------------------

# Letter inputed by the user
def try_letter(letter,hm):
    word = hm.word
    hidden_word = hm.hidden_word
    for l in re.finditer(letter,word):
        hidden_word = hidden_word[:(l.start())*2] + letter + hidden_word[2*(l.start())+1:]
        hm.hidden_word = hidden_word
        hm.n_rounds +=1
        if "_" not in hidden_word:
            stats(hm)
        return hm.hidden_word
    hm.wrong_attempts.append(letter)
    hm.n_mistakes +=1
    hm.n_rounds +=1
    return False


# Word inputed by the user
def try_word(attempt,hm):
    word = hm.word
    if word == attempt:
        return True
    hm.wrong_attempts.append(attempt)
    hm.n_mistakes +=2
    hm.n_rounds +=1
    return False

#-------------------------------------------------------------------------------------------

#----------------------------------------Progress-------------------------------------------

# Returns the progress of the word
def get_word(hm):
    print(hm.hidden_word)


# Returns the list of the failed attempts
def get_wrg_attempts(hm):
    print(hm.wrong_attempts)


# Contains the progress of the hanged man
def hangman(hm):
    fails = hm.n_mistakes
    if fails == 0:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("             |")
        print("             |")
        print("             |")
        print("             |")
        print("_____________|")
        fails +=1

    elif fails == 1:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("    O        |")
        print("             |")
        print("             |")
        print("             |")
        print("_____________|")

    elif fails == 2:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("    O        |")
        print("    |        |")
        print("             |")
        print("             |")
        print("_____________|")

    elif fails == 3:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("    O        |")
        print("    |\       |")
        print("             |")
        print("             |")
        print("_____________|")

    elif fails == 4:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("    O        |")
        print("   /|\       |")
        print("             |")
        print("             |")
        print("_____________|")

    elif fails == 5:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("    O        |")
        print("   /|\       |")
        print("     \       |")
        print("             |")
        print("_____________|")

    elif fails == 6:
        print(f"You made {fails}/6 mistakes")
        print("    __________")
        print("    |        |")
        print("    |        |")
        print("    O        |")
        print("   /|\       |")
        print("   / \       |")
        print("             |")
        print("_____________|")


# Returns end of game stats
def stats(hm):
    print("\n---Game Over!---")
    print(f"Word: {hm.word}")
    print(f"Rounds: {hm.n_rounds}")
    print(f"Mistakes: {hm.n_mistakes}")
    print("----------------\n")
    print("Want to play again?")
    restart = input("'Y' if yes or 'N' if no: ")
    if restart == 'Y':
        hm.word = None
        hm.wrong_attempts.clear()
        hm.n_rounds = 0
        hm.n_mistakes = 0
    elif restart == 'N':
        vw.playing = False

#-------------------------------------------------------------------------------------------