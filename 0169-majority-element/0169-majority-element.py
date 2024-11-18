from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        max_item = float('-inf')
        max_num = None

        for key in freq:
            if freq[key] > max_item:
                max_item = freq[key]
                max_num = key
            
        return max_num