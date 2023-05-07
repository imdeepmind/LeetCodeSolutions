class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        
        matches = []
        
        for index, num in enumerate(sorted_nums):
            if num == target:
                matches.append(index)
        
        return matches
        