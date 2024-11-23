class Solution:
    def findBlock(self, matrix, target):
        l, r = 0, len(matrix) - 1

        while l <= r:
            m = l + ((r-l) // 2)

            arr = matrix[m]

            if arr[0] <= target <= arr[-1]:
                return arr
            else:
                if arr[0] > target:
                    r = m - 1
                else:
                    l = m + 1
        
        return []

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        block = self.findBlock(matrix, target)

        if not block:
            return False
        
        l, r = 0, len(block) - 1

        while l <= r:
            m = l + ((r-l)//2)

            if block[m] > target:
                r = m - 1
            elif block[m] < target:
                l = m + 1
            else:
                return True

        return False    
        