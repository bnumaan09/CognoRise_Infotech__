import random
import tkinter as tk

def play(user_choice):
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    result_text = determine_winner(user_choice, computer_choice)
    
    result_label.config(text=f"Computer chose {computer_choice}. {result_text}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Create the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Create buttons for each choice
rock_button = tk.Button(root, text="Rock", command=lambda: play("rock"))
paper_button = tk.Button(root, text="Paper", command=lambda: play("paper"))
scissors_button = tk.Button(root, text="Scissors", command=lambda: play("scissors"))

# Pack the buttons onto the window
rock_button.pack()
paper_button.pack()
scissors_button.pack()

# Label to show the result
result_label = tk.Label(root, text="Make your choice!")
result_label.pack()

# Start the GUI event loop
root.mainloop()
