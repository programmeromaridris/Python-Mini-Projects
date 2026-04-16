import random

user_wins = 0
cpu_wins = 0

while True:
    rps = ["rock", "paper", "scissors"]
    user_input = input("Enter a choice (rock, paper, scissors), or Q to quit: ").lower()
    if user_input == "q":
        quit()
    else:
        if user_input not in rps:
            print("Please enter a valid choice.")
            continue
        else: 
            cpu_choice = random.choice(rps)
            if user_input == cpu_choice:
                print("It's a tie! You both chose " + user_input + ".")
            elif user_input == "rock" and cpu_choice == "scissors":
                print("You win! Rock beats scissors")
                user_wins += 1
            elif user_input == "paper" and cpu_choice == "rock":
                print("You win! Paper beats rock")
                user_wins += 1
            elif user_input == "scissors" and cpu_choice == "paper":
                print("You win! Scissors beats paper")
                user_wins += 1
            else:
                print("You lose! " + cpu_choice + " beats " + user_input)
                cpu_wins += 1