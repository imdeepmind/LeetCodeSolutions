class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, slow2, fast = 0, 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break
        
        return slow2