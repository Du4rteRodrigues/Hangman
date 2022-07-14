from Models.models import hangman as hm
from Models.models import mode as md
import Controllers.progress as prgctr
import Controllers.attempts as atpctr
import Controllers.checks as chkctr
import Controllers.operations as opctr

def playing():
    return True


while playing:
    if md == None:
        opctr.get_modes()
        md = int(input("Choose a mode: "))

    # Normal
    if md == 1:
        if hm.word == None:
            word = input(str("Select a word: "))
            if chkctr.check_type(word):
                opctr.save_word(word,hm)
            else:
                print("The word must contain only letters")
        else:
            opctr.clear_terminal()
            opctr.get_operations()
            prgctr.hangman(hm)
            prgctr.get_word(hm)
            print("")
            prgctr.get_wrg_attempts(hm)
            operation = (input("\nChoose an operation: "))


            # End Game
            if operation == '0':
                print("Game Over!\n")
                hm.word = None

            # Try letter
            elif operation == '1':
                letter = str(input("Try a letter: "))
                if chkctr.check_length(letter):
                    if not chkctr.check_misses(letter, hm):
                        if not chkctr.check_letter(letter,hm,md):
                            print(f"'{letter}' isn't in the word :(")
                            chkctr.check_fails(hm)
                        else:
                            print("You are correct! :)")
                    else:
                        print("You already tried that! Try again")
                else:
                    print("Try only 1 letter!")

            # Try Word
            elif operation == '2':
                attempt = str(input("Try a word: "))
                if not chkctr.check_misses(attempt, hm):
                    if not chkctr.check_word(attempt,hm,md):
                    # if not atpctr.try_word(attempt,hm):
                        print(f"'{attempt}' isn't the word :(")
                        chkctr.check_fails(hm)
                    else:
                        print("You are correct! :)")
                        prgctr.stats(hm,md)
                else:
                    print("You already tried that! Try again")

            
            else:
                print("That operations doesn't exist :/")
    
    # Random
    elif md == 2:
        pass

    # Calculator
    elif md == 3:
        pass
    
