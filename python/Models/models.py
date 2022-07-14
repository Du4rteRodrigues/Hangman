from array import array

class hangman():
    word = None
    wrong_attempts = []
    n_mistakes = 0
    n_rounds = 0
    def __init__(self, word:str, hidden_word:str, wrong_attempts:array, n_mistakes:int, n_rounds:int) -> None:
        self.word = word
        self.hidden_word = hidden_word
        self.wrong_attempts = wrong_attempts
        self.n_mistakes = n_mistakes
        self.n_rounds = n_rounds

mode = None