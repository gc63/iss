class Solution:
    def add_solution(self, board, ans):
        temp = []
        for row in board:
            temp.append(''.join(row))
        ans.append(temp)

    def is_safe(self, row, col, board, n):
        # Check the column
        for i in range(row):
            if board[i][col] == 'Q':
                return False

        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False

        # Check upper right diagonal
        for i, j in zip(range(row, -1, -1), range(col, n)):
            if board[i][j] == 'Q':
                return False

        return True

    def solve(self, row, ans, board, n):
        if row == n:
            self.add_solution(board, ans)
            return

        for col in range(n):
            if self.is_safe(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(row + 1, ans, board, n)
                board[row][col] = '.'

    def solve_n_queens(self, n):
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []

        self.solve(0, ans, board, n)
        return ans

def main():
    n = int(input("Enter the size of the chessboard: "))
    solution = Solution()
    ans = solution.solve_n_queens(n)

    print("\nSolutions for N-Queens problem:")
    for solution in ans:
        for row in solution:
            print(row)
        print()
    print(len(ans))
if __name__ == "__main__":
    main()
