import views as vw

# Returns the progress of the word
def get_word(hm):
    print(hm.hidden_word)
    return(hm.hidden_word)



# Returns the list of the failed attempts
def get_wrg_attempts(hm):
    print(hm.wrong_attempts)
    return(hm.wrong_attempts)


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