from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()

        l = r = 0
        while len(nums) > r:
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)

            if l > q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
                l += 1
            
            r += 1

        return res
