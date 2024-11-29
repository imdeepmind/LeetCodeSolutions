from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        freq = defaultdict(int)
        maxf = 0
        max_val = 0

        while len(s) > r:
            freq[s[r]] += 1
            maxf = max(maxf, freq[s[r]])

            while (r - l + 1) - maxf > k:
                freq[s[l]] -= 1
                l += 1
            
            max_val = max(max_val, r-l+1)
            r += 1

        return max_val
