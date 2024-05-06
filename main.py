from tkinter import *
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.players = ["O", "X"]
        self.player = random.choice(self.players)

        self.buttons = [ #intializing 2D array
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]

        self.label = Label(master, text=self.player + " turn", font=('consolas', 40))
        self.label.pack(side="top")

        self.reset_button = Button(master, text="Restart", font=('consolas', 20), command=self.new_game)
        self.reset_button.pack(side="bottom")

        self.frame = Frame(master)
        self.frame.pack()

        for row in range(3):
            for column in range(3):
                self.buttons[row][column] = Button(self.frame, text="", font=('console', 40), width=5, height=2,
                command=lambda row=row, column=column: self.next_turn(row, column))
                self.buttons[row][column].grid(row=row, column=column)

    def next_turn(self, row, column):
        if self.buttons[row][column]['text'] == "" and not self.check_winner():
            if self.player == self.players[0]:
                self.buttons[row][column]['text'] = self.player

                if not self.check_winner():
                    self.player = self.players[1]
                elif self.check_winner() == "Tie":
                    self.label.config(text="TIE")
                elif self.check_winner():
                    self.label.config(text=(self.players[0] + " wins"))

            else:
                self.buttons[row][column]['text'] = self.player

                if not self.check_winner():
                    self.player = self.players[0]
                elif self.check_winner() == "Tie":
                    self.label.config(text="TIE")
                elif self.check_winner():
                    self.label.config(text=(self.players[1] + " wins"))

    def check_winner(self):
        for row in range(3):
            if self.buttons[row][0]['text'] == self.buttons[row][1]['text'] == self.buttons[row][2]['text'] != "":
                self.highlight_winner(row, 0, row, 1, row, 2)
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == \
                    self.buttons[2][column]['text'] != "":
                self.highlight_winner(0, column, 1, column, 2, column)
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            self.highlight_winner(0, 0, 1, 1, 2, 2)
            return True
        elif self.buttons[2][0]['text'] == self.buttons[1][1]['text'] == self.buttons[0][2]['text'] != "":
            self.highlight_winner(2, 0, 1, 1, 0, 2)
            return True
        elif not self.empty_spaces():
            for row in range(3):
                for column in range(3):
                    self.buttons[row][column].config(bg="purple")
            return "Tie"
        else:
            return False

    def highlight_winner(self, *args):
        for i in range(0, len(args), 2):
            self.buttons[args[i]][args[i + 1]].config(bg="green")

    def new_game(self):
        self.player = random.choice(self.players)
        self.label.config(text=self.player + " turn")

        for row in range(3):
            for column in range(3):
                self.buttons[row][column].config(text="", bg="#F0F0F0")

    def empty_spaces(self):
        # check how many empty spaces that we have
        spaces = 9
        for row in range(3):
            for column in range(3):
                if self.buttons[row][column]['text'] != "":
                    spaces = spaces - 1

        return spaces != 0

root = Tk()
my_game = TicTacToe(root)
root.mainloop()









