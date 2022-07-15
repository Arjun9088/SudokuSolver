class SudokuSolver:

    __board = None
    __BOARD_SIZE = None
    
    def __init__(self, board):
        self.BOARD_SIZE = 9
        self.board = board

    def solve(self):
        return self.solveBoard()

    def __solveBoard(self):
        for row in range(0, self.BOARD_SIZE):
            for column in range(0, self.BOARD_SIZE):
                if self.board[row][column] == 0:
                    for num in range(1, self.BOARD_SIZE+1):
                        if self.isValidPlacement(num, row, column):
                            self.board[row][column] = num
                            if self.solveBoard():
                                return True
                            else:
                                self.board[row][column] = 0
                    return False
        return True

    def __isValidPlacement(self, number, row, column):
        return not self.is_number_present_in_row(number, row) and not self.is_number_present_in_column(number, column) and not self.is_number_present_in_grid(number, row, column)
    
    def __is_number_present_in_row(self, number, row):
        for col in range(0, self.BOARD_SIZE):
            if self.board[row][col] == number :
                return True
        return False

    def __is_number_present_in_column(self, number, column):
        for row in range(0, self.BOARD_SIZE):
            if self.board[row][column] == number:
                return True
        return False

    def __is_number_present_in_grid(self, number, row, column):
        local_row = row - (row % 3)
        local_column = column - (column % 3)
        for r in range(local_row, local_row + 3):
            for c in range(local_column, local_column + 3):
                if(self.board[r][c] == number):
                    return True
        return False

    def printBoard(self):
        for i in range(0, self.BOARD_SIZE):
            for j in range(0, self.BOARD_SIZE):
                if j !=0 and (j+1) % 3 == 0:
                    print(self.board[i][j],end=" | ")
                else:
                    print(self.board[i][j],end=" ")
            print()


if __name__ == "__main__":
    print("main")