# Darius Corbin
# 04/15/2023
# Rock Paper Scissors
# Human v. Bot
# GUI Version

import tkinter as tk
import random

class RockPaperScissors(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Rock Paper Scissors")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.lbl_player_choice = tk.Label(self, text="Your Choice: ")
        self.lbl_player_choice.pack()

        self.rock_button = tk.Button(self, text="Rock", command=lambda: self.play("rock"))
        self.rock_button.pack()

        self.paper_button = tk.Button(self, text="Paper", command=lambda: self.play("paper"))
        self.paper_button.pack()

        self.scissors_button = tk.Button(self, text="Scissors", command=lambda: self.play("scissors"))
        self.scissors_button.pack()

        self.lbl_computer_choice = tk.Label(self, text="Computer Choice: ")
        self.lbl_computer_choice.pack()

        self.lbl_result = tk.Label(self, text="")
        self.lbl_result.pack()

        self.quit_button = tk.Button(self, text="Quit", command=self.master.destroy)
        self.quit_button.pack()

    def play(self, player_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])

        self.lbl_player_choice.configure(text="Your Choice: " + player_choice.capitalize())
        self.lbl_computer_choice.configure(text="Computer Choice: " + computer_choice.capitalize())

        if player_choice == computer_choice:
            result = "Tie!"
        elif player_choice == "rock" and computer_choice == "scissors":
            result = "You Win!"
        elif player_choice == "paper" and computer_choice == "rock":
            result = "You Win!"
        elif player_choice == "scissors" and computer_choice == "paper":
            result = "You Win!"
        else:
            result = "You Lose!"

        self.lbl_result.configure(text=result)

if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(master=root)
    game.mainloop()
