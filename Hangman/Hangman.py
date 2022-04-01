import random
from christmaslist import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_compleation = "_" * len(word)
    guessed= False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Welcome to Hangman")
    print(display_hangman(tries))
    print(word_compleation)
    print("\n")
    while not guessed and tries >0:
        guess = input("Type your guessed letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("Letter has already been guessed", guess)
            elif guess not in word:
                print(guess,"incorrect guess")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Correct Guess", guess, "is in the word :)")
                guessed_letters.append(guess)
                word_as_list = list(word_compleation)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_compleation = "".join(word_as_list)
                if"_" not in word_compleation:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess,"is not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_compleation = word
        else:
            print("Not a valid guess")
        print(display_hangman(tries))
        print(word_compleation)
        print("\n")
    if guessed:
        print("You win")
    else:
        print("Out of tries, the word was"+ word + ".")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    word = get_word()
    play(word)
    while input("Play again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)

if __name__ == "__main__":
    main()