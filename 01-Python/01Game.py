import random

round = 0
total_round = 5
users = ["Alice", "Bob", "Charlie"]

# Fix scoreboard keys
score_board = {"Alice": 0, "Bob": 0, "Charlie": 0}

while round < total_round:
    print(f"\n--- Round {round + 1} ---")
    
    random_number = random.randint(1, 9)
    print("Random number is:", random_number)

    for user in users:
        user_input = int(input(f"{user}, guess a number (1-9): "))

        if user_input < 1 or user_input > 9:
            print("Please enter a number between 1 and 9.")
        elif user_input == random_number:
            print("Correct guess!")
            score_board[user] += 1   
        else:
            print("No match!")

    round += 1   

# Final Scores
print("\nFinal Scores:")
for user, score in score_board.items():
    print(f"{user}: {score}")