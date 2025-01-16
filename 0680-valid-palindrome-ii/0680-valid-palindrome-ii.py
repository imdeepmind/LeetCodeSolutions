class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrime(l, r):
            while r > l:
                if s[l] != s[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        n = len(s)
        l, r = 0, n - 1

        while r > l:
            if s[l] != s[r]:
                return is_palindrime(l+1, r) or is_palindrime(l, r-1)
            
            l += 1
            r -= 1
        
        return True