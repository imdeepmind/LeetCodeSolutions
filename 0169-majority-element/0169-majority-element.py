from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mapper = defaultdict(int)

        for num in nums:
            mapper[num] += 1
        
        biggest_value = float('-inf')
        biggest_freq = 0

        for key, value in mapper.items():
            if value > biggest_freq:
                biggest_freq = value
                biggest_value = key
        
        return biggest_value