from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
        
        res = []

        for key, value in counter.items():
            if value > len(nums) / 3:
                res.append(key)
        
        return res