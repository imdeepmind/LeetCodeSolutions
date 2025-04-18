class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0, 0, 0]

        for num in nums:
            buckets[num] += 1
        
        j = 0

        for index, bucket in enumerate(buckets):
            for _ in range(bucket):
                nums[j] = index
                j += 1
        
