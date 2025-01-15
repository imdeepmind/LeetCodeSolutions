import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = re.sub(r"\W", "", s)
        s = s.replace("_", "")

        n = len(s)

        for i in range(n//2):
            opp = n - i - 1

            if s[i] != s[opp]:
                return False
        
        return True