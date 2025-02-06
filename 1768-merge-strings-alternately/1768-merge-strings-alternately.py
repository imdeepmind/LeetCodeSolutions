class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""

        while len(word1) > i or len(word2) > j:
            if len(word1) > i:
                res += word1[i]
                i += 1
            
            if len(word2) > j:
                res += word2[j]
                j += 1
        
        return res