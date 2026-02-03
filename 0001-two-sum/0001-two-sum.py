class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapper = {}

        for index, num in enumerate(nums):
            delta = target - num

            if delta in mapper and mapper[delta] != index:
                return [mapper[delta], index]
            
            mapper[num] = index
        
        return [-1, -1]