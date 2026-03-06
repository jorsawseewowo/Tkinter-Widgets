import random
import tkinter as tk

def play_round(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        result = "You win!"
    else:
        result = "Computer wins!"

    return f"You chose {user_choice}, computer chose {computer_choice}. {result}"

def play(user_choice):
    result_text.set(play_round(user_choice))

root = tk.Tk()
root.title("Rock Paper Scissors")

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14))
result_label.pack(pady=20)
button_frame = tk.Frame(root)
button_frame.pack()

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("rock"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("paper"))
scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("scissors"))

rock_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissors_btn.grid(row=0, column=2, padx=10)
root.mainloop()
