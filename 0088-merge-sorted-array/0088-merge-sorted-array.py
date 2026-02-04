class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a1, a2 = m - 1, n - 1
        k = len(nums1) - 1

        while a2 >= 0:
            if a1 >= 0 and nums1[a1] > nums2[a2]:
                nums1[k] = nums1[a1]
                a1 -= 1
            else:
                nums1[k] = nums2[a2]
                a2 -= 1

            k -= 1
