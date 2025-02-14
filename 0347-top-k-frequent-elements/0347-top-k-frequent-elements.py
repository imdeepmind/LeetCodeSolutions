from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper = defaultdict(int)

        for num in nums:
            mapper[num] += 1
        
        bucket = [[] for i in range(len(nums))]

        for key, value in mapper.items():
            bucket[value-1].append(key)
        
        res = []

        for i in range(len(bucket)-1,-1,-1):
            for item in bucket[i]:
                if bucket[i] != 0:
                    res.append(item)
            
        
        return res[:k]
