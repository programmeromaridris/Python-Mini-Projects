import random

top_of_range = input("You are playing a number guessing game! To quit, type 'q'. Type a number:")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()
else:    
    print("Please type a number next time.")
    quit()
        
        

random_number = random.randint(1, top_of_range)

while True:
    user_guess = input("Take a guess:")
    if user_guess.isdigit():
      user_guess = int(user_guess)
    elif user_guess == "q":
     print("You quit the game! The correct number was:" + str(random_number))
     quit() 
      
    else:
        print("Please type a number next time.")
        continue
    
    
    if user_guess == random_number:
        print("You got it correct!")
        break
    else:
        print("Sorry, you got it wrong! Keep going!")
        continue
    

    

