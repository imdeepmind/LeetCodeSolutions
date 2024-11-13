class Solution:
    def isHappy(self, n: int) -> bool:
        def to_array(n):
            nums = []
            while n > 0:
                nums = [n%10] + nums
                n = n//10
            
            return nums

        def productSum(nums):
            return sum([num**2 for num in nums])

        if n == 1 or n == 7:
            return True

        nums = to_array(n)

        while len(nums) > 1:
            n = productSum(nums)
            
            print(n)
            if n == 1 or n == 7:
                return True
            nums = to_array(n)
        
        if len(nums) == 1 and nums[0] == 1:
            return True
        
        return False
        
        
