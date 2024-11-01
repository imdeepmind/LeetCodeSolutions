class Solution:
    def countBits(self, n: int) -> List[int]:
        resp = []

        for i in range(n+1):
            ans = 0

            while i:
                if i % 2:
                    ans += 1
                
                i = i >> 1

            resp.append(ans)
        
        return resp
