import time

playing = input("Are you playing? (yes/no) ")

if playing != "yes":
    time.sleep(0.7)
    print("Please come back when you are ready to play.")
    quit()

time.sleep(0.7)
print("Okay, let's play! :)")

score = 0  
answer = input("Who is the best football player in the world?")

if answer.lower() != "ronaldo":
    time.sleep(0.7)
    print("Wrong! The correct answer is Ronaldo.")
    quit()
    
score = 10
time.sleep(0.7)
print("Your score is: " + str(score))

answer = input("What is the largest country in the world?")
if answer.lower() != "russia":
    time.sleep(0.7)
    print("Wrong! The correct answer is Russia.")
    quit() 
score = 20
time.sleep(0.7)
print("Your score is: " + str(score) + ". Next round is double points!")

answer = input("Arachnophobia is the fear of what?")
if answer.lower() != "spiders":
    time.sleep(0.7)
    print("Wrong! The correct answer is Spiders.")
    quit()
score = 40
print("Your score is: " + str(score) + ". Last round wins all!")

answer = input("What is the capital of Canada?")
if answer.lower() != "ottawa":
    time.sleep(0.7)
    print("Wrong! The correct answer is Ottawa.")
    quit()
score = 100
time.sleep(0.7)
print("Congratulations! Your final score is: " + str(score) + ". You are a quiz master!")     

   
