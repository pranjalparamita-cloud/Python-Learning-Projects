print("--------------------Dice Game--------------------")

import random
print("Kya tum khelna chahte ho? (No/Yes)")
choice=input()
if choice=="No":
    print("Exiting the game. Goodbye!")
    exit()
else:
    while True:
        print("Game start hua...")
        players = []
        num_players = int(input("Kitne players khel rahe hain? Enter number of players: "))
        for i in (range(1, num_players + 1)):
            players.append(f"Player {i}")
        scores = {player: 0 for player in players}
        rounds = 5
        for round in range(1, rounds + 1):
            print(f"\n--- Round {round} ---")
            for player in players:
                input(f"{player}, press Enter to roll the dice...")
                roll = random.randint(1, 6)
                scores[player] += roll
                print(f"{player} rolled a {roll}. Total score: {scores[player]}")
        total_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        print("\n--- Final Scores ---")
        for player, score in total_scores:
            print(f"{player} wins the game with a score of: {score}")
            if score > 20:
                print(f"Congratulations {player}! Tum toh champion nikle !")
        print("Thank you for playing the Dice Game!")
        play_again=input("Phirse kheloge? (yes/no): ").lower()
        if play_again!="yes":
            break
    print("\nGame Khatam hua.......Bye Bye!")
    
