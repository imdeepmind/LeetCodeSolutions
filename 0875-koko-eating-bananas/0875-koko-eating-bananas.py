class Solution:
    def canFinishAllBananas(self, piles, k=1):
        totalHour = 0
        for pile in piles:
            totalHour += math.ceil(pile / k)
        
        return totalHour

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0

        while l <= r:
            m = l + ((r-l)//2)

            totalTime = self.canFinishAllBananas(piles, m)

            if totalTime <= h:
                r = m - 1
                res = m
            else:
                l = m + 1

        return res