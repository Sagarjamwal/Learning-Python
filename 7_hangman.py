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

  while not guessed and tries > 0:
     guess=input("Please Guess a Letter or Word: ").upper()

     if len(guess)==1 and guess.isalpha():

       if guess in guessed_letters:
          print("You already guessed ",guess)

       elif guess not in word:
          print(guess,"is not in the word.")
          tries-=1
          guessed_letters.append(guess)

       else:
          print("Good Job!",guess,"is in the word!")
          guessed_letters.append(guess)

          word_as_list=list(word_completion)
          indices=[i for i,letter in enumerate(word) if letter == guess]
          for index in indices:
            word_as_list[index]=guess

          word_completion="".join(word_as_list)

          if "_" not in word_completion:
            guessed=True

     elif len(guess)==len(word) and guess.isalpha():

        if guess in guessed_words:
           print("You already guessed ",guess)

        elif guess!=word:
           print(guess,"is not the word")
           tries-=1
           guessed_words.append(guess)

        else:
           guessed=True
           word_completion=word

     else:
        print("Not a Valid Guess.")

     print(display_hangman(tries))
     print(word_completion)
     print("\n")

  if guessed:
    print("Congratulations,you guessed the word! You win!")
  else:
    print("Sorry you lost the word was:"+word+"Maybe next time")

def main():
 word=get_word()
 play(word)
 while input("Play Again?!(Y/N)").upper()=="Y":
  word=get_word()
  play(word)

if __name__=="__main__":
 main()