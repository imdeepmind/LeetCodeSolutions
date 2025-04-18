from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)

        for word in strs:
            key = "".join(sorted(word))
            mapper[key].append(word)
        
        res = []

        for _, value in mapper.items():
            res.append(value)
        
        return res