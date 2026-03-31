from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for p1, p2 in trust:
            outgoing[p1] += 1
            incoming[p2] += 1
        
        for i in range(n):
            p = i + 1

            if outgoing[p] == 0 and incoming[p] == n-1:
                return p
        
        return -1