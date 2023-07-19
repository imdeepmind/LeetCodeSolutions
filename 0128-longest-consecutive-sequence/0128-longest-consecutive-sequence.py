class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        hash = {}
        seq = 0
        
        for num in nums:
            hash[num] = 1
        
        for num in nums:
            if num - 1 not in hash:
                length = 0
                
                while num+length in hash:
                    length += 1
                
                seq = max(seq, length)
        
        return seq