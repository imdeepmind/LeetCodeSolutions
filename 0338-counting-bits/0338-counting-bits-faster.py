class Solution:
    def countBits(self, n: int) -> List[int]:
        resp = [0] * (n+1)
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i

            resp[i] = 1 + resp[i - offset]
            
        return resp
