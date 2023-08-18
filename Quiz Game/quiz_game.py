print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")
points = 0

if playing.lower() != "yes":
    quit()
print ("Okay! Let's play :)")    

answer = input("what does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    points +=1
else:
    print("wrong answer!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    points +=1
else:
    print("wrong answer!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    points +=1
else:
    print("wrong answer!")

answer = input("what does PSU stand for? ").lower()
if answer == "power supply":
    print("Correct!")
    points +=1
else:
    print("wrong answer!")

print("You got " + str(points) + " points")
print("You got " + str((points/4)* 100 ) + "%")