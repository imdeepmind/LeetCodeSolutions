class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub_arr = nums[0]
        cur_sum = 0
        
        for num in nums:
            if cur_sum < 0:
                cur_sum = 0
            
            cur_sum += num
            
            sub_arr = max(sub_arr, cur_sum)
        
        return sub_arr