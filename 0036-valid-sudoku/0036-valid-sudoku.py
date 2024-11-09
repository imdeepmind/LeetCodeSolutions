class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash = {}

        for num in nums:
            if num != ".":
                if num not in hash:
                    hash[num] = 0
                else:
                    return True
        
        return False
    def getAllColumns(self, board):
        res = []
        for i in range(9):
            level = []
            for j in range(9):
                level.append(board[j][i])

            res.append(level)

        return res

    def getAllSubboxes(self, board):
        res = []
        for i in range(0, 9, 3):
            sub_rows = board[i:i+3]

            for j in range(0, 9, 3):
                level = []
                for x in range(3):
                    sub_columns = sub_rows[x][j:j+3]
                    level += sub_columns

                res.append(level)

        return res

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.containsDuplicate(row):
                return False
        
        for column in self.getAllColumns(board):
            if self.containsDuplicate(column):
                return False

        for sub in self.getAllSubboxes(board):
            if self.containsDuplicate(sub):
                return False

        return True
