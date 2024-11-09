class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter_s = {}

        for c in s:
            counter_s[c] = counter_s[c] + 1 if c in counter_s else 1

        for c in t:
            counter_s[c] = counter_s[c] - 1 if c in counter_s else 1
                
        for key in counter_s:
            if counter_s[key] >= 1:
                return False
        
        return True
