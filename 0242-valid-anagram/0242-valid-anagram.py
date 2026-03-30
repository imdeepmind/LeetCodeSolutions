class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chrs = [0] * 26
        delta = 97

        if len(s) != len(t):
            return False

        for c in s:
            chrs[ord(c) - delta] += 1

        for c in t:
            chrs[ord(c) - delta] -= 1


        for val in chrs:
            if val != 0:
                return False

        return True