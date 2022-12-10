class Solution:
    cache = {}
    
    def takeStep2(self, curr, maxStep):
        if curr == maxStep:
            return 1
        
        if curr > maxStep:
            return 0
        
        if curr in self.cache:
            return self.cache[curr]
        
        res = self.takeStep2(curr+1, maxStep) + self.takeStep2(curr+2, maxStep)
        
        self.cache[curr] = res
        
        return res

        
    def climbStairs(self, n: int) -> int:
        self.cache = {}
        
        return self.takeStep2(0, n)