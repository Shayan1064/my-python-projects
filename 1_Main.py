 # Its My first Project

# Its Snake, Water, Gun Game

# 1 for Snake
# 2 for Water 
# 0 for gun

import random

print("Welcome to Snake, Water, Gun Game!")
print("1 = Snake, 2 = Water, 0 = Gun")

choice = input("Type 'Play' to start or 'Exit' to quit: ")

if choice.lower() == "play":
    computer = random.choice([0, 1, 2])  # 0=Gun, 1=Snake, 2=Water
    you = int(input("Enter your choice: "))

    print(f"Computer chose: {computer}")

    if computer == you:
        print("Draw!")
    elif (computer == 1 and you == 2) or (computer == 2 and you == 0) or (computer == 0 and you == 1):
        print("Computer Wins!")
    else:
        print("You Win!")
else:
    print("You quit the game.")


