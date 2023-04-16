# Darius Corbin
# 04/14/2023
# Tic Tac Toe Game
# 1 v 1
# (GUI Version)



import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.turn = "X"
        self.board = [" "]*9

        self.create_board()

    def create_board(self):
        self.button_list = []
        for i in range(9):
            button = tk.Button(self.master, text=" ", width=10, height=5, command=lambda index=i:self.button_click(index))
            button.grid(row=i//3, column=i%3)
            self.button_list.append(button)

        reset_button = tk.Button(self.master, text="Reset", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3)

    def button_click(self, index):
        if self.board[index] == " ":
            self.board[index] = self.turn
            self.button_list[index].config(text=self.turn)
            if self.check_win():
                self.show_winner()
            else:
                if self.turn == "X":
                    self.turn = "O"
                else:
                    self.turn = "X"

    def check_win(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return True

        # check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return True

        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return True

        if self.board[2] == self.board[4] == self.board[6] != " ":
            return True

        # check if board is full
        if " " not in self.board:
            self.show_winner()

        return False

    def show_winner(self):
        winner = ""
        if " " not in self.board:
            winner = "No one"
        else:
            winner = self.turn

        messagebox.showinfo("Winner", f"{winner} wins!")
        self.reset_game()

    def reset_game(self):
        self.turn = "X"
        self.board = [" "]*9
        for button in self.button_list:
            button.config(text=" ")


root = tk.Tk()
tic_tac_toe = TicTacToe(root)
root.mainloop()
