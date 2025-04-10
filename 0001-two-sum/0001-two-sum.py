class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for index, num in enumerate(nums):
            mapper[num] = index
        
        for index, num in enumerate(nums):
            delta = target - num

            if delta in mapper and index != mapper[delta]:
                return index, mapper[delta]
        
        return -1, -1
