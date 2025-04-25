class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        start, total = 0, 0
        min_value = float('inf')

        for end, num in enumerate(nums):
            total += num

            while total >= target:
                min_value = min(min_value, end - start + 1)
                total -= nums[start]
                start += 1
        
        return min_value if min_value != float('inf') else 0