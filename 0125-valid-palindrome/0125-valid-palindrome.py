import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r"[^a-zA-Z0-9]", "", s)

        start, end = 0, len(s) - 1

        while end > start:
            if s[start] != s[end]:
                return False
            
            start += 1
            end -= 1
        
        return True