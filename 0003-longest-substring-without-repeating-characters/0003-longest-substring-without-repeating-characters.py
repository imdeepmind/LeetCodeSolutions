class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mapper = set()
        max_length = 0
        start = 0
        
        for end, c in enumerate(s):
            while c in mapper:
                mapper.remove(s[start])
                start += 1
            
            mapper.add(c)

            max_length = max(len(mapper), max_length)

        return max_length