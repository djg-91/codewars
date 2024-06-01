'''
https://www.codewars.com/kata/586c0909c1923fdb89002031

    Task
        The game consists of a grid (7 columns and 6 rows) and two players that take turns to drop their discs. 
        The pieces fall straight down, occupying the next available space within the column. 
        The objective of the game is to be the first to form a horizontal, vertical, or diagonal line 
        of four of one's own discs.

        Your task is to create a Class called Connect4 that has a method called play which takes one argument 
        for the column where the player is going to place their disc.
   
    Rules
        If a player successfully has 4 discs horizontally, vertically or diagonally then you should 
        return "Player n wins!” where n is the current player either 1 or 2.

        If a player attempts to place a disc in a column that is full then you 
        should return ”Column full!” and the next move must be taken by the same player.

        If the game has been won by a player, any following moves should return ”Game has finished!”.

        Any other move should return ”Player n has a turn” where n is the current player either 1 or 2.
        
        Player 1 starts the game every time and alternates with player 2.

        The columns are numbered 0-6 left to right.
'''


import numpy as np

class Connect4():

    def __init__(self):
        self.board = np.full((7, 6), '0', dtype=str)
        self.player = '2'
        self.finished = False

    def play(self, col):
        self.player = '2' if self.player == '1' else '1'
        
        if self.finished:
            return "Game has finished!"
        
        try:
            col_lst = list(self.board[col])
            played_pos = col_lst.index('0')
            col_lst[played_pos] = self.player
            self.board[col] = col_lst
        except:
            self.player = '2' if self.player == '1' else '1'
            return "Column full!"

        def check_win():

            # Extract both diagonals of a position
            def extract_diags(pos):
                return np.diag(self.board, pos[1]-pos[0]), np.diag(self.board[::-1,:], pos[1]+pos[0]-len(self.board)+1)

            # Check vertical
            if str(self.player)*4 in ''.join([str(x) for x in col_lst]):
                return True

            # Check horizontal
            if str(self.player)*4 in ''.join([str(x) for x in self.board[:,played_pos]]):
                return True

            # Check diagonals
            for diag in extract_diags((col, played_pos)):
                if str(self.player)*4 in ''.join(list(diag)):
                    return True

        if check_win():
            self.finished = True
            return f"Player {self.player} wins!"

        return f"Player {self.player} has a turn"