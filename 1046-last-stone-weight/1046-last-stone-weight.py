class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)

            if s1 < s2:
                heapq.heappush(stones, s1 - s2)

        stones.append(0)
        return abs(stones[0])
