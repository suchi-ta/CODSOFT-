import tkinter as tk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")
        self.user_score = 0
        self.computer_score = 0

        
        self.score_label = tk.Label(root, text="Score - You: 0, Computer: 0")
        self.score_label.pack(pady=10)

        self.instructions_label = tk.Label(root, text="Choose your move:")
        self.instructions_label.pack(pady=10)

        
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack(pady=5)

        
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=10)

       
        self.play_again_button = tk.Button(root, text="Play Again", command=self.reset_game, state=tk.DISABLED)
        self.play_again_button.pack(pady=10)

    def play(self, user_move):
        computer_move = random.choice(["rock", "paper", "scissors"])
        self.result_label.config(text=f"Your move: {user_move}\nComputer's move: {computer_move}")

        # Determine the winner
        if user_move == computer_move:
            self.result_label.config(text=self.result_label.cget("text") + "\nIt's a tie!")
        elif (user_move == "rock" and computer_move == "scissors") or \
             (user_move == "paper" and computer_move == "rock") or \
             (user_move == "scissors" and computer_move == "paper"):
            self.user_score += 1
            self.result_label.config(text=self.result_label.cget("text") + "\nYou win!")
        else:
            self.computer_score += 1
            self.result_label.config(text=self.result_label.cget("text") + "\nYou lost!")

        self.score_label.config(text=f"Score - You: {self.user_score}, Computer: {self.computer_score}")
        self.play_again_button.config(state=tk.NORMAL)

    def reset_game(self):
        self.user_score = 0
        self.computer_score = 0
        self.score_label.config(text="Score - You: 0, Computer: 0")
        self.result_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)

# Create the main window
if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissorsGame(root)
    root.mainloop()
