name = input("What's your name: ")
print("Welcome", name,"to this adventure!")

answer = input("You are in a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or you can swim accross it. Type walk to walk around or swim to swim accross: ").lower()

    if answer == "swim":
        print("You swim accross and you got eaten by a alligator. ")
    elif answer == "walk":
        print("You walked many miles, ran out of water and you lost the game. ")
    else:
        print("Not a valid option. You lose. ")

elif answer == "right": 
    answer = input("You come to a bridge, it looks wobly, do you want to cross it or head back (cross/back)? ").lower()

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge, you meet a stranger. Do you talk to them (yes/no)?").lower()

        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and you lose!")
        else:
            print("Not a vali option. ")

    else:
        print("Not a valid option. You lose. ")
else:
    print("Not a valid option. You lose. ")

print("Thank you for trying", name)