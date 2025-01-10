class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for index, num in enumerate(nums):
            if (target - num) in mapper:
                return index, mapper[target-num]

            mapper[num] = index
            
        return -1,-1
        