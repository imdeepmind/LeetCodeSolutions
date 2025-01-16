class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for index, num in enumerate(nums):
            delta = target - num

            if delta in mapper:
                return [index, mapper[delta]]
            
            mapper[num] = index
        
        return [-1, -1]