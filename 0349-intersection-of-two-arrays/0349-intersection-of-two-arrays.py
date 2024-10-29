class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = {}

        for num in nums1:
            hash[num] = 0
        
        commonHash = {}

        for num in nums2:
            if num in hash:
                commonHash[num] = 0
        
        return [num for num in commonHash]
