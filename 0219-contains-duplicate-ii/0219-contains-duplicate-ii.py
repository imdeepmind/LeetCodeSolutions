class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapper = {}

        for index, num in enumerate(nums):
            if num in mapper:
                if abs(mapper[num] - index) <= k:
                    return True

            mapper[num] = index
        
        return False
