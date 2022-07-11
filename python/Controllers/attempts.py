import re
import Controllers.progress as prgctr

# Letter inputed by the user
def try_letter(letter,hm):
    word = hm.word
    hidden_word = hm.hidden_word
    for element in word:
        for l in re.finditer(letter,word):
            hidden_word = hidden_word[:(l.start())*2] + letter + hidden_word[2*(l.start())+1:]
            hm.hidden_word = hidden_word
            hm.n_rounds +=1
        if "_" not in hidden_word:
            prgctr.stats(hm)
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