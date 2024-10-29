from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash = Counter(nums1)
        
        common = []
        for num in nums2:
            if num in hash and hash[num] > 0:
                common.append(num)
                hash[num] -= 1
        
        return common
