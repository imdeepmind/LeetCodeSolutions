from collections import defaultdict

class Solution:
    def generateKey(self, word):
        return "".join(sorted(word))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _hash = defaultdict(list)

        for word in strs:
            _hash[self.generateKey(word)].append(word)
        
        res = []

        for key, value in _hash.items():
            res.append(value)

        return res
