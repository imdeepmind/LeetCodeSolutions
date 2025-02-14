from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = defaultdict(list)

        for word in strs:
            mapper["".join(sorted(word))].append(word)
        
        res = []
        for _, values in mapper.items():
            res.append(values)
        
        return res
