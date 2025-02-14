from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = defaultdict(int)

        for num in nums:
            mapper[num] += 1
        
        bucket = [[] for _ in range(len(nums))]

        for key, value in mapper.items():
            bucket[value-1].append(key)
        
        res = []

        print(bucket)

        for i in range(len(bucket)-1, -1, -1):
            b = bucket[i]

            for n in b:
                res.append(n)
                # if n != 0:

        return res[:k]
