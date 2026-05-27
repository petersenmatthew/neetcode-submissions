class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = [set() for _ in range(9)]        # list of sets
        blocks = [[set() for _ in range(3)] for _ in range(3)]
        # column[0] is a set of all nums in first col
        for row_index, row in enumerate(board):
            row_set = set()
            for col_index, num in enumerate(row):
                if num != ".":  # Only process actual numbers
                    r_block, c_block = row_index // 3, col_index // 3
                    if num in row_set or num in columns[col_index] or num in blocks[r_block][c_block]:
                        return False
                    row_set.add(num)
                    columns[col_index].add(num)
                    blocks[r_block][c_block].add(num)
        return True
# (row, col): (2,2), (5, 2), (8, 2), (2, 5), (5, 5), (8, 5)

# row + 1 // 3 == 0 and col + 1 // 3 == 0, then check the square