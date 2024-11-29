from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)

        if nt > ns: return ""
        if s == t: return s

        tFreq = Counter(t)
        windowFreq = {}

        have, need = 0, len(tFreq)

        res, res_len = [-1, -1], float('inf')

        l = 0
        for i in range(len(s)):
            c = s[i]
            windowFreq[c] = 1 + windowFreq.get(c, 0)

            if c in tFreq and tFreq[c] == windowFreq[c]:
                have += 1
            
            while have == need:
                if (i-l+1) < res_len:
                    res_len = i-l+1
                    res = [l, i]
                
                windowFreq[s[l]] -= 1

                if s[l] in tFreq and windowFreq[s[l]] < tFreq[s[l]]:
                    have -= 1
                
                l += 1
            
        return s[res[0]:res[1]+1] if res_len < float('inf') else ""





        # windowFreq = Counter(s[:nt])

        # res_len = float('inf')
        # res = ""

        # while ns > r:
        #     print(tFreq, windowFreq, s[l:r+1])
        #     if self.isSame(tFreq, windowFreq):
        #         res_len = min(res_len, len(s[l:r+1]))
        #         print(s[l:r+1])
        #         l += 1
        #         r = l + nt

        #         windowFreq = Counter(s[l:r])

            
        #     if res == nt:
        #         return res
            
        #     windowFreq[s[r]] += 1

        #     r += 1

        #     if r == ns and l < ns-nt:
        #         l += 1
        #         r = l + nt - 1

        #         windowFreq = Counter(s[l:r])



        # print(res_len)
        # return res