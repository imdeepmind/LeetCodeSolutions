from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sl = len(s)
        tl = len(t)

        if sl != tl:
            return False
        
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        for c in s:
            s_freq[c] += 1
        
        for c in t:
            t_freq[c] += 1
        
        for key, value in s_freq.items():
            if value != t_freq[key]:
                return False
        
        for key, value in t_freq.items():
            if value != s_freq[key]:
                return False
        
        return True