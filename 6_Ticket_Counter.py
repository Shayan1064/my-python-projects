print("Welcome To Kund National Park")
name = input("Please Enter Your Name: ")
print("Hello", name, "Please Select Your Tickets\n")

amount = 0

while True:
    print("1) Roller Coaster : RS 500")
    print("2) Ferris Wheel : RS 300")
    print("3) Bumper Cars : RS 500")
    print("4) Swing Ride : RS 400")
    print("5) Drop Tower : RS 1000")
    print("6) Train : RS 500")
    print("7) Pirate Ship : RS 200")
    print("8) Water Slide : RS 300")
    print("9) Haunted House : RS 500")
    print("10) Teacup Ride : RS 700")
    print("11) Q to EXIT")

    choice = int(input("Press: "))
    

    if choice == 1:
        print("You selected Roller Coaster")
        amount += 500
    elif choice == 2:
        print("You selected Ferris Wheel")
        amount += 300
    elif choice == 3:
        print("You selected Bumper Cars")
        amount += 500
    elif choice == 4:
        print("You selected Swing Ride")
        amount += 400
    elif choice == 5:
        print("You selected Drop Tower")
        amount += 1000
    elif choice == 6:
        print("You selected Train")
        amount += 500
    elif choice == 7:
        print("You selected Pirate Ship")
        amount += 200
    elif choice == 8:
        print("You selected Water Slide")
        amount += 300
    elif choice == 9:
        print("You selected Haunted House")
        amount += 500
    elif choice == 10:
        print("You selected Teacup Ride")
        amount += 700
    elif choice == 11:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please select between 1-11.")

print("\nTotal Amount to Pay: RS", amount)
