import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-x for x in stones]

        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            y = heapq.heappop(self.stones)
            x = heapq.heappop(self.stones)

            if x != y:
                heapq.heappush(self.stones, y-x)
       
        return self.stones[0] * -1 if len(self.stones) > 0 else 0
