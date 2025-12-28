class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _hash = {}

        for index, num in enumerate(nums):
            _hash[num] = index
        
        for index, num in enumerate(nums):
            delta = target - num

            if delta in _hash and _hash[delta] != index:
                return [index, _hash[delta]]
        
        return [-1, -1]