class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        
        freq1 = {}
        freq2 = {}
        
        for index, ch in enumerate(s):
            if ch in freq1:
                freq1[ch] += 1
            else:
                freq1[ch] = 1
            
            if t[index] in freq2:
                freq2[t[index]] += 1
            else:
                freq2[t[index]] = 1
        
        return freq1 == freq2
        