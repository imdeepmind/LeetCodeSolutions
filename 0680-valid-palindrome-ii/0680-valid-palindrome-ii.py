class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(start, end):
            while end > start:
                if s[start] != s[end]:
                    return False
                
                end -= 1
                start += 1

            return True
        
        start, end = 0, len(s) - 1

        while end > start:
            if s[start] != s[end]:
                return isPalindrome(start+1, end) or isPalindrome(start, end-1)

            start += 1
            end -= 1
        
        return True
