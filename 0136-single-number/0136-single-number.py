class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        
        for num in nums:
            xor = num ^ xor
            
        return xor