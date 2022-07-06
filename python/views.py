from models import hangman as hm
import controllers as ctr

def playing():
    return True


while playing:
    if hm.word == None:
        word = input(str("Select a word: "))
        if ctr.check_type(word):
            ctr.save_word(word,hm)
        else:
            print("The word must contain only letters")
    else:
        print("\nChoose operation '0' for help.")
        operation = (input("Choose an operation: "))

        # Help
        if operation == '0':
            ctr.get_operations()

        # End Game
        elif operation == 'x':
            print("Game Over!\n")
            ctr.clear_terminal()
            hm.word = None

        # Try letter
        elif operation == '1':
            letter = str(input("Try a letter: "))
            if ctr.check_length(letter):
                if not ctr.check_misses(letter, hm):
                    if not ctr.try_letter(letter,hm):
                        print(f"'{letter}' isn't in the word :(")
                        ctr.check_fails(hm)
                    else:
                        print("You are correct! :)")
                else:
                    print("You already tried that! Try again")
            else:
                print("Try only 1 letter!")

        # Try Word
        elif operation == '2':
            attempt = str(input("Try a word: "))
            if not ctr.check_misses(attempt, hm):
                if not ctr.try_word(attempt,hm):
                    print(f"'{attempt}' isn't the word :(")
                    ctr.check_fails(hm)
                else:
                    print("You are correct! :)")
                    ctr.stats(hm)
            else:
                print("You already tried that! Try again")

        # Get Word Progress
        elif operation == '3':
            ctr.get_word(hm)

        # Get Hangman progress
        elif operation == '4':
            ctr.hangman(hm)

        # Get Wrong Attempts
        elif operation == '5':
            ctr.get_wrg_attempts(hm)
        
        else:
            print("That operations doesn't exist :/")
