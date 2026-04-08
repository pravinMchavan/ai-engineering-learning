# a = 10
# b = 0

# try:
#     c = a / b
#     print("last")
# except ZeroDivisionError as e:
#     print("Exception message:", e)

# finally:
#     print("This will always execute.")

import random

round = 0
total_round = 5
users = ["Alice", "Bob", "Charlie"]

score_board = {"Alice": 0, "Bob": 0, "Charlie": 0}


def generate_random_number():
    return random.randint(1, 9)


def get_user_input(user):
    try:
        user_input = int(input(f"{user}, guess a number (1-9): "))
        
        if user_input < 1 or user_input > 9:
            raise ValueError("Number out of range")
        
        return user_input

    except ValueError:
        print(" Invalid input! Please enter a number between 1 and 9.")
        return None


def verify_number(user, user_input, random_number):
    if user_input is None:
        return

    if user_input == random_number:
        print(" Correct guess!")
        score_board[user] += 1
    else:
        print(" No match!")

# Game loop
while round < total_round:
    print(f"\n--- Round {round + 1} ---")
    
    random_number = generate_random_number()
    print(" Random Number:", random_number)

    for user in users:
        user_input = get_user_input(user)
        verify_number(user, user_input, random_number)

    round += 1

# Final scores
print("\n Final Scores:")
for user, score in score_board.items():
    print(f"{user}: {score}")