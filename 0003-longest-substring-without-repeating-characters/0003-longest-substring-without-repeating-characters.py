class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        mapper = set()
        max_length = 0
        start = 0

        for end, c in enumerate(s):
            while s[end] in mapper:
                mapper.remove(s[start])
                start += 1
            
            mapper.add(s[end])
            max_length = max(max_length, len(mapper))

        return max_length
