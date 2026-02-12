print("-----------Lets play Rock, Paper, Scissors!-----------")
import random
choices = ["👊  rock","📃  paper","✂️  scissors"]
computer_choice = random.choice(choices)
user_choice = input("Enter your choice (👊  rock, 📃  paper, ✂️  scissors): ")
if user_choice not in ["rock", "paper", "scissors"]:
    print("Invalid choice! Please choose rock, paper, or scissors.")
else:
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {user_choice}")

    if computer_choice == user_choice:
        print("It's a tie!")
    elif (computer_choice == "👊  rock" and user_choice == "scissors"):
        print("Computer wins!")
    elif(computer_choice == "📃  paper" and user_choice == "rock"):
        print("Computer wins!")
    elif (computer_choice == "✂️  scissors" and user_choice == "paper"):
        print("Computer wins!")
        
    else:
        print("You win!")