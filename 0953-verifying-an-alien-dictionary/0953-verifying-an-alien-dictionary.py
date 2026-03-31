class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapper = {o:idx for idx, o in enumerate(order)}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]

            for idx, c in enumerate(w1):
                if idx == len(w2):
                    return False
                
                if c != w2[idx]:
                    if mapper[c] > mapper[w2[idx]]:
                        return False
                    break
            
        return True
