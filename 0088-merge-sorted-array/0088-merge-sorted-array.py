class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        res = len(nums1) - 1
        p, q = m - 1, n - 1

        while p >= 0 or q >= 0:
            if p >= 0 and q >= 0:
                if nums1[p] > nums2[q]:
                    nums1[res] = nums1[p]
                    p -= 1
                else:
                    nums1[res] = nums2[q]
                    q -= 1
            else:
                if p >= 0 and q < 0:
                    nums1[res] = nums1[p]
                    p -= 1
                else:
                    nums1[res] = nums2[q]
                    q -= 1
            
            res -= 1
