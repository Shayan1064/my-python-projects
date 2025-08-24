import random

target = random.randint(1, 100) 


while(True):
    userinput=input("Guess the Number OR Quit : ")
    if(userinput.lower()=="Quit".lower()):
        break


    userinput=int(userinput)
    if(userinput==target):
        print("Correct You WIN!")
    elif(userinput<target):
        print("Your Guess is Small, Please Guess Large")
    else:
        print("Your Guess is Large, Please Guess Small")

print("---GAME OVER!---")