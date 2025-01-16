class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while r > l:
            alpha = numbers[l] + numbers[r]

            if target == alpha:
                return l+1, r+1

            if target > alpha:
                l += 1
            else:
                r -= 1
        
        return -1, -1

