import random
choices = ["rock","paper","scissors"]
c=random.choice(choices)# c for computer
u=input("Enter Rock , Paper or Scissors :").lower() #u for user choice

print(f"You chose {u}.  Computer chose {u} ")

if u == c:
    print("It's a Tie")
elif u == "rock" and c == "paper":
    print(f"Wow You Win!: {u} beats {c}")
elif u == "scissors" and c =="paper":
    print(f"Wow You Win!: {u} beats {c}")
elif u == "paper" and u == "rock":
    print(f"Wow You Win!: {u} beats {c}")
else:
    print("You Lost to a Computer: LOL LOL LOL ")


