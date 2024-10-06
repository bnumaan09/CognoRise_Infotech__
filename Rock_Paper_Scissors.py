import random

# Possible moves
choices = ['rock', 'paper', 'scissors']

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "win"
    else:
        return "lose"

# Initialize scores
rounds_to_win = 3
user_score = 0
computer_score = 0

while user_score < rounds_to_win and computer_score < rounds_to_win:
    # ... (your main game logic here)
    
    # Check if someone has won
    if user_score == rounds_to_win:
        print("You won the best of five series!")
    elif computer_score == rounds_to_win:
        print("Computer won the best of five series!")
        
    # Computer's random choice
    computer_choice = random.choice(choices)
  
    user_choice = input("Enter your Choice( Rock,Paper,Scissors): ")
    print(f"You entered: {user_choice}")

    
    # Display the choices
    print(f"Computer chose: {computer_choice}")
    
    # Determine the result
    result = determine_winner(user_choice, computer_choice)
    
    if result == "win":
        print("You win!")
        user_score += 1
    elif result == "lose":
        print("You lose!")
        computer_score += 1
    else:
        print("It's a tie!")
    
    # Display the score
    print(f"Score: You {user_score} - Computer {computer_score}")
    
    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        break

# Final score display
print(f"Final Score: You {user_score} - Computer {computer_score}")
print("Thanks for playing!")


