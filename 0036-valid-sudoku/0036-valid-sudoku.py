class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board: return True

        def is_column_valid():
            for column in board:
                mapper = {}

                for item in column:
                    if item in (",", "."): continue
                    if item in mapper: return False
                    mapper[item] = 1
            
            return True
        
        def is_valid_row():
            ROWS, COLS = len(board), len(board[0])

            for c in range(COLS):
                mapper = {}
                for r in range(ROWS):
                    alpha = board[r][c]

                    if alpha in (",", "."): continue
                    if alpha in mapper: return False
                    mapper[alpha] = 1
            
            return True
        
        def is_valid_sub_box():
            res = []
            for i in range(0, 9, 3):
                sub_rows = board[i:i+3]

                for j in range(0, 9, 3):
                    level = []
                    for x in range(3):
                        sub_columns = sub_rows[x][j:j+3]
                        level += sub_columns

                    res.append(level)
            
            for column in res:
                mapper = {}

                for item in column:
                    if item in (",", "."): continue
                    if item in mapper: return False
                    mapper[item] = 1
            
            return True

        
        return is_column_valid() and is_valid_row() and is_valid_sub_box()
                    