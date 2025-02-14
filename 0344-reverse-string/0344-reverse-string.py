class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)

        for i in range(n // 2):
            opp = n - i - 1
            s[i], s[opp] = s[opp], s[i]
        