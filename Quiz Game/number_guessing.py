import random

top_of_range = input("Type a number: ")
guesses = 0

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger next time.")
        quit()

else:
    print("Please type a number next time.")
    quit()

random_number = random.randint(0,top_of_range)

while True:
    user_guess = input("Make a guess: ")
    guesses += 1
    
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time.")
        continue

    if user_guess == random_number:
        print("You got it!")
        print("Number of guesses:", guesses, "guesses")
        break
    elif user_guess > random_number:
        print("Type a number lesser than your last guess")
    else:
        print("type a number higher than the last guess")
        
        
