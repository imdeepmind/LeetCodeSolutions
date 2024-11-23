class Solution:
    def scoreOfString(self, s: str) -> int:
        res = 0

        for index, c in enumerate(s):
            if index+1 != len(s):
                res += abs(ord(c) - ord(s[index+1]))
        
        return res
        