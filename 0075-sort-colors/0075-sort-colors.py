class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]

        for num in nums:
            buckets[num] += 1

        k = 0
        for i in range(len(nums)):
            while buckets[k] <= 0:
                k += 1

            nums[i] = k
            buckets[k] -= 1
