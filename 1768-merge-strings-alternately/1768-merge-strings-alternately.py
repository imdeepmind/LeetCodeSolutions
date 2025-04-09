class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = ""
        i, j = 0, 0
        n1, n2 = len(word1), len(word2)

        while n1 > i or n2 > j:
            if n1 > i:
                new += word1[i]
                i += 1
            
            if n2 > j:
                new += word2[j]
                j += 1
        
        return new