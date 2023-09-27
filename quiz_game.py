print("Welcome to this quiz!")

playing = input("Do you want to play?(yes/no) ") 

if playing.lower() != "yes":
    quit()

print("Ok! Let's play: ")
score = 0

answer = input("what does CPU stand for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does GPU Stand for? ")
if answer.lower() == "graphic processing unit":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What does PS stand for? ")
if answer.lower() == "power source":
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

print("You got " +str(score) + " questions correct!")
print("You got " +str(score/4)*100+ "%")

