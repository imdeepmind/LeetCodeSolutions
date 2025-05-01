class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        start = 0
        mapper = set()
        max_length = 0
        
        for current in range(len(s)):
            while s[current] in mapper:
                mapper.remove(s[start])
                start += 1
            
            mapper.add(s[current])
            max_length = max(max_length, current - start + 1)
        
        return max_length