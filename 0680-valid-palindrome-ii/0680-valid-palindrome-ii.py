class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(start, end):
            while end > start:
                if s[start] != s[end]:
                    return False
                
                start += 1
                end -= 1
            
            return True
        
        start, end = 0, len(s) - 1

        while end > start:
            if s[start] != s[end]:
                return is_palindrome(start + 1, end) or is_palindrome(start, end - 1)
            
            start += 1
            end -= 1
        
        return True