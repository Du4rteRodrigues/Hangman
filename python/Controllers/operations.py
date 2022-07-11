from Models.models import hangman as hm
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
    hidden_word = ""
    slot = "_ "
    space = "- "
    for element in word:
        if element == "-":
            hidden_word += space
        hidden_word += slot
    hm.hidden_word = hidden_word
    clear_terminal()
    return True


# Clears the terminal
def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')