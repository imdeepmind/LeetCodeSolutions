from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for i in range(len(s)):
            s_freq[s[i]] += 1
            t_freq[t[i]] += 1
        
        for key, value in s_freq.items():
            if value != t_freq[key]:
                return False
            
        return True
