class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_len = 0
        max_str = ""

        for i in range(n):
            l, r = i-1, i+1

            while l >= 0 and n > r and  s[l] == s[r]:
                if len(s[l:r+1]) > max_len:
                    max_len = len(s[l:r+1])
                    max_str = s[l:r+1]
                
                l -= 1
                r += 1

            if i > 0 and s[i-1] == s[i]:
                if len(s[i-1:i+1]) > max_len:
                    max_len = len(s[i-1:i+1])
                    max_str = s[i-1:i+1]
                

        return max_str

