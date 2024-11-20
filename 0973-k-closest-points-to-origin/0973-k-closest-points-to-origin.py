class Solution:
    def calculateDistance(self, point: List[int]):
        return math.sqrt(((0 - point[0]) ** 2) + ((0 - point[1]) ** 2))

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.points = [[self.calculateDistance(point), point[0], point[1]] for point in points]

        heapq.heapify(self.points)

        res = []
 
        for _ in range(k):
            item = heapq.heappop(self.points)
            res.append(item[1:])

        return res