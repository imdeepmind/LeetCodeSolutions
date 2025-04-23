from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incomingMapper = defaultdict(int)
        outgoingMapper = defaultdict(int)

        for t in trust:
            outgoingMapper[t[0]] += 1
            incomingMapper[t[1]] += 1
        
        for i in range(1, n+1):
            if incomingMapper[i] == n-1 and outgoingMapper[i] == 0:
                return i
                
        return -1