import random
import time
print("----------------------------------------Welcome to Tambola Game-------------------------------")
print("Rules:")
print("1. Each player gets a ticket with 9 random numbers between 1 and 90.")
print("2. Numbers from 1 to 90 will be called out randomly.")
print("3. Players need to mark the numbers on their tickets.")
print("Do u want to play the game? (No/Yes)")
choice=input()
if choice=="No":
    print("Exiting the game. Goodbye!")
    exit()
else:
    while True:
        print("Starting the game...")
        players=int(input("Enter number of players: "))
        tickets=[]
        for i in range(players):
            ticket=random.sample(range(1,91),9)
            tickets.append(ticket)
        print("\n--- TICKETS ---")
        for i in range(players):
            print("Player",i+1,"ticket:",tickets[i])
        numbers=list(range(1,91))
        random.shuffle(numbers)
        print("\n--- GAME STARTED ---")
        for num in numbers:
            print("Number called:",num)
            time.sleep(1)
            ans=input("Did anyone win? (yes/no): ").lower()
            if ans=="yes":
                winner=int(input("Enter winning player number: "))
                print(f"Waooo!the player {winner} has won the game!..........Congratulations!")
                break
        play_again=input("Do you want to play again? (yes/no): ").lower()
        if play_again!="yes":
            break
    print("\nGame Over")
    
