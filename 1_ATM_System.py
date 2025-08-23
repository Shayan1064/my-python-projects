name=input(("Enter Your Name Please : "))
print("Welcome to ATM System : ",name)
password=input("Please Enter Your Password : ")
Balance=10000
if(name.lower()=="Shayan".lower() and password=="Shayan2115"):
        while(True):
            
            print("Press in the following : ")
            print("1: Checking Balance")
            print("2: Deposit Money")
            print("3: Withdraw Money")
            print("4: Exit!")
            Press=int(input())
            if(Press==1):
                print("Your Balance is : ",Balance)
            elif(Press==2):
                    deposite=int(input("Deposit Amount : "))
                    Balance+=deposite
                    print("New Balance : ",Balance)
            elif(Press==3):
                    Withdraww=int(input("Withdraw Amount : "))
                    if(Balance<Withdraww):
                        print("Not Enough Amount")
                    else:
                        Balance-=Withdraww
                        print("New Balance : ",Balance)
            elif(Press==4):
                print("Thank You For  Using ATM")
                break
            else:
                print("Please Press Valid Option")
else:
    print("Username OR Password is Incorrect")