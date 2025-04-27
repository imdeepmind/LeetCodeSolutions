import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)
        
        val = None
        for _ in range(k):
            val = heapq.heappop(nums)
        
        return val * -1