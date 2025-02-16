class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for index, num in enumerate(nums):
            mapper[num] = index
        
        for index, num in enumerate(nums):
            alpha = target - num

            if alpha in mapper and mapper[alpha] != index:
                return index, mapper[alpha]
        
        return -1, -1