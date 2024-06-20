import random

def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose again (rock, paper, or scissors).")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win!")
    else:
        print("Computer wins!")

def play_again():
    while True:
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again in ["yes", "no"]:
            return again == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def display_score(user_score, computer_score):
    print(f"\nCurrent Score - You: {user_score}, Computer: {computer_score}\n")

def rock_paper_scissors():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        display_result(user_choice, computer_choice, winner)
        display_score(user_score, computer_score)

        if not play_again():
            print("Thanks for playing! Final Score - You: {}, Computer: {}".format(user_score, computer_score))
            break

if __name__ == "__main__":
    rock_paper_scissors()
