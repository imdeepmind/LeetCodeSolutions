class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1)-1, len(word2)-1
        p, q = 0, 0
        res = ""

        while n1 >= p or n2 >= q:
            if n1 >= p:
                res += word1[p]
                p += 1
            
            if n2 >= q:
                res += word2[q]
                q += 1
        
        return res
