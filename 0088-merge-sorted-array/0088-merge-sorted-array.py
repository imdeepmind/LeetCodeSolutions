class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j = 0, 0
        
        while len(nums1) >= i+1 and len(nums2) >= j+1:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                j += 1
            
            i += 1
        
        for i in range(n):
            del nums1[-1]
        
        
        while len(nums2) >= j+1:
            nums1.append(nums2[j])
            j += 1
