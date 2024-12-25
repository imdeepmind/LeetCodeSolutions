class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1

        while j > i:
            alpha = numbers[i] + numbers[j]

            if alpha > target:
                j -= 1
            elif alpha < target:
                i += 1
            else:
                return i+1, j+1
        
        return [-1, -1]