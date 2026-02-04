class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        anchor1, anchor2 = 0, 0
        n1, n2 = len(word1), len(word2)

        while n1 > anchor1 or n2 > anchor2:
            first = word1[anchor1] if n1 > anchor1 else ""
            second = word2[anchor2] if n2 > anchor2 else ""

            res += first + second

            if first:
                anchor1 += 1
            
            if second:
                anchor2 += 1

        return res