from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def getKey(word):
            return "".join(sorted(word))
        
        hash = defaultdict(list)

        for word in strs:
            hash[getKey(word)].append(word)
        
        resp = []

        for key, value in hash.items():
            resp.append(value)
        
        return resp