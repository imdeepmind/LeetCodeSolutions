class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = [
            set(list("qwertyuiop")),
            set(list("asdfghjkl")),
            set(list("zxcvbnm"))
        ]

        matched = []

        for word in words:
            exists = True
            for c in word:
                if c.lower() not in rows[0]:
                    exists = False
            
            if exists:
                matched.append(word)
        
        for word in words:
            exists = True
            for c in word:
                if c.lower() not in rows[1]:
                    exists = False
            
            if exists:
                matched.append(word)
        
        for word in words:
            exists = True
            for c in word:
                if c.lower() not in rows[2]:
                    exists = False
            
            if exists:
                matched.append(word)
        
        return matched