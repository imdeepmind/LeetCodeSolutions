import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.stones = [-stone for stone in stones]
        heapq.heapify(self.stones)

        while len(self.stones) > 1:
            element1 = heapq.heappop(self.stones)
            element2 = heapq.heappop(self.stones)

            if element1 != element2:
                heapq.heappush(self.stones, element1-element2)
        
        return abs(self.stones[0]) if self.stones else 0