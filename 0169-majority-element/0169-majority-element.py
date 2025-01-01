from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_item = 0
        max_item_value = 0
        mapper = {}

        for num in nums:
            mapper[num] = mapper.get(num, 0) + 1
            if mapper[num] > max_item:
                max_item = mapper[num]
                max_item_value = num
            
        return max_item_value