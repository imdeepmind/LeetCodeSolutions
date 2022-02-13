class Solution:
    def isPalindrome(self, x: int) -> bool:
        t = str(x)
        return t == t[::-1]