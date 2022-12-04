import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^0-9a-zA-Z]+', '', s)
        s = s.replace(' ', '')
        
        k = len(s) - 1
        
        for i in range(len(s) // 2):
            if s[i] != s[k]:
                return False
            
            k -= 1
        
        return True