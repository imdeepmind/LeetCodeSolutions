class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = {}

        for num in nums:
            mapper[num] = 1 + mapper.get(num, 0)

        bucket = [[] for _ in range(len(nums))]

        for key, value in mapper.items():
            bucket[value-1].append(key)
        
        res = []

        for i in range(len(bucket)-1, -1, -1):
            for b in bucket[i]:
                res.append(b)
        
        return res[:k]

