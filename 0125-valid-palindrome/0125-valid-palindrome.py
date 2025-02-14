import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace(" ", "").replace("_", "")
        s = re.sub("\W", "", s)

        n = len(s)

        for i in range(n // 2):
            opp = n - i - 1

            if s[i] != s[opp]:
                return False
        
        return True