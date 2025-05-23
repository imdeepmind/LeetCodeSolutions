from collections import defaultdict

class Solution:
    def generateKey(self, word):
        return "".join(sorted(word))

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = defaultdict(list)

        for word in strs:
            freq[self.generateKey(word)].append(word)
        
        resp = []
        for key, value in freq.items():
            resp.append(value)
        
        return resp