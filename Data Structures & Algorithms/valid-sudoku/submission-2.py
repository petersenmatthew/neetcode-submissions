class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       # cols = array of 9 sets 
       # rows = array of 9 sets
       cols = [set() for _ in range(9)]
       rows = [set() for _ in range(9)] 
       sub_boxes = [[set() for _ in range(3)] for _ in range(3)]


       for row_index, row in enumerate(board):
            for col_index, cur_num in enumerate(row):

                # empty tile
                if cur_num == ".":
                    continue
                
                if cur_num in cols[col_index]:
                    return False
                cols[col_index].add(cur_num)
                
                if cur_num in rows[row_index]:
                    return False
                rows[row_index].add(cur_num)
                
                sb_index = (row_index // 3, col_index // 3)

                if cur_num in sub_boxes[sb_index[0]][sb_index[1]]:
                    return False
                sub_boxes[sb_index[0]][sb_index[1]].add(cur_num)
       return True

                #0: 012 1: 345 2:678
