import random 
a=random.randint(1,100) # a stores a ramdom integer value from 1 to 100

print("I'm thinking of a number between 1 and 100 \n Can you guess it?: ")

attempts=0
while True:
    guess=int(input("Enter your guess: "))
    if guess < a:
        print("Ohh No! Your guess is lower than my number ")
        attempts=attempts+1
    elif guess > a:
        print("Oh No! Your guess is higher than my number ")
        attempts=attempts+1
    elif guess==a:
        print(f"Congrats you guessed my number: {a} in {attempts} guesses")
        break 
    else:
        print("Please enter a valid integer ")
