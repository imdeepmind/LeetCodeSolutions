class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        
        needle_l = len(needle)
        
        for i in range(0, len(haystack)-(needle_l-1)):
            target = haystack[i:i+needle_l]
            
            if target == needle:
                return i
            
        return -1
