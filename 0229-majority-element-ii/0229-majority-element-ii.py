from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        mapper = defaultdict(int)

        for num in nums:
            mapper[num] += 1

            if len(mapper) <= 2:
                continue
            
            new = defaultdict(int)
            for key, value in mapper.items():
                if value > 1:
                    new[key] = value-1
            
            mapper = new
        
        for key in mapper:
            if nums.count(key) > len(nums) // 3:
                res.append(key)
        
        return res