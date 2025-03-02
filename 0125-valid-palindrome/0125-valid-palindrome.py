import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower().replace("_", "")
        s = re.sub(r"\W", "", s)

        for i in range(len(s) // 2):
            opp = len(s) - i - 1

            if s[i] != s[opp]:
                return False
        
        return True