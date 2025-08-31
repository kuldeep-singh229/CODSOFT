import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def main():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors! 🎮")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            print("\nFinal Scores:")
            print(f" You: {user_score}")
            print(f" Computer: {computer_score}")
            print("Thanks for playing! 👋")
            break

        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f" You chose: {user_choice}")
        print(f" Computer chose: {computer_choice}")

        winner = get_winner(user_choice, computer_choice)

        if winner == "tie":
            print(" It's a tie! 😐")
        elif winner == "user":
            print(" You win! 🎉")
            user_score += 1
        else:
            print(" Computer wins! 🤖")
            computer_score += 1

        print(f" Score -> You: {user_score} | Computer: {computer_score}\n")

if __name__ == "__main__":
    main()
