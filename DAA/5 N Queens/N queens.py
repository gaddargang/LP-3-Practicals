class NQueens:
    def __init__(self, N):
        self.N = N
        self.board = [['.' for _ in range(N)] for _ in range(N)]
        self.solutions = []

    def is_safe(self, row, col):
        # Check same column
        for i in range(row):
            if self.board[i][col] == 'Q':
                return False

        # Check upper-left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 'Q':
                return False

        # Check upper-right diagonal
        for i, j in zip(range(row, -1, -1), range(col, self.N)):
            if self.board[i][j] == 'Q':
                return False

        return True

    def solve(self, row=0):
        if row == self.N:
            solution = [''.join(row) for row in self.board]
            self.solutions.append(solution)
            return
        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.solve(row + 1)
                self.board[row][col] = '.'

    def solve_nqueens(self):
        self.solve()
        return self.solutions

def print_solutions(solutions):
    for i, solution in enumerate(solutions, 1):
        print(f"Solution {i}:")
        for row in solution:
            print(row)
        print()

if __name__ == "__main__":
    N = int(input("Enter the size of the chessboard: "))
    if N <= 0:
        print("Invalid input. Please enter a positive integer.")
    else:
        n_queens = NQueens(N)
        solutions = n_queens.solve_nqueens()
        print(f"Total solutions for {N}-Queens: {len(solutions)}")
        print_solutions(solutions)
