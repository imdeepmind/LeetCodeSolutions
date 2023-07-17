import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = s.replace(' ', '')
        
        for idx, c in enumerate(s):
            if c != s[-(idx+1)]:
                return False
        
        return True
