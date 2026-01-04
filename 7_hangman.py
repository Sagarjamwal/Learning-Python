# Hangman is a guessing game which is played by guessing the a word by
# suggesting letters with some number of guesses usually around 6 before
# the hangman figure is completed and the user loses 
# You can also watch the video from where I learnt it by clicking this link
# https://www.youtube.com/watch?v=m4nEnsavl6w

import random
words=['hello','python','world','apple']

def get_word():
    word=random.choice(words)
    return word.upper()

def play(word):
 word_completion="_"*len(word)
 guessed=False
 guessed_letters=[]
 guessed_words=[]
 tries=6
 print("Let's Play HangMan!: ")
 print(display_hangman(tries))
 print(word_completion)
 print("\n")
 while not guessed and tries >0:
    guess=("Please Guess a Letter or Word: ").upper()
    if len(guess)==1 and guess.isalpha():
       if guess in guessed_letters:
          print("You already guessed ",guess)
       elif guess not in word:
          print(guess,"is not in the word.")
          tries-=1
       guessed_letters.append(guess) 
          
    
    elif len(guess)==len(word) and guess.isalpha():
       
    else:
       print("Not a Valid Guess.")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    













 def display_hangman(tries):
    stages=["""
            ~~~~~~~~~~~~~~~
            |     |
            |     O
            |   \\|//
            |     |
            |    / \
            ~~~~~~~~~~~~~~~
            """,
            """
            ~~~~~~~~~~~~~~~
            |     |
            |     O
            |   \\|//
            |     |
            |    / 
            ~~~~~~~~~~~~~~~
            """,
            """
            ~~~~~~~~~~~~~~~
            |     |
            |     O
            |   \\|//
            |     |
            |
            ~~~~~~~~~~~~~~~
            """,
            """
            ~~~~~~~~~~~~~~~
            |     |
            |     O
            |   \\|//
            |     
            |
            ~~~~~~~~~~~~~~~
            """,
            """
            ~~~~~~~~~~~~~~~
            |     |
            |     O
            |   
            |     
            |
            ~~~~~~~~~~~~~~~
            """,
            """
            ~~~~~~~~~~~~~~~
            |     |
            |     
            |   
            |     
            |
            ~~~~~~~~~~~~~~~
            """,
            """
            ~~~~~~~~~~~~~~~
            |     
            |     
            |   
            |     
            |
            ~~~~~~~~~~~~~~~
            """]
    return stages[tries]
 