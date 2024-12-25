import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub('[^0-9a-zA-Z]+', '', s)

        if s == "":
            return True

        for i in range(len(s)//2+1):
            alpha = len(s) - (i+1)

            if s[i] != s[alpha]:
                return False
        
        return True