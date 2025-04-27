class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        longest = 0

        for num in numbers:
            if (num - 1) not in numbers:
                length = 1

                while (num + length) in numbers:
                    length += 1
                
                longest = max(length, longest)
        
        return longest
