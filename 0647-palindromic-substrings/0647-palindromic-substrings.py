class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        if n == 1:
            return 1

        res = []

        for i in range(n):
            l, r = i, i

            while l >= 0 and n > r and  s[l] == s[r]:
                res.append(s[l:r+1])
                
                l -= 1
                r += 1

            l, r = i, i+1

            while l >= 0 and n > r and  s[l] == s[r]:
                res.append(s[l:r+1])

                l -= 1
                r += 1

        return len(res)

