class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        
        for p in strs[0]:
            delta = res + p
            matched = True

            for word in strs[1:]:
                if not word.startswith(delta):
                    matched = False
                    break
            
            if matched:
                res += p
            else:
                break
        
        return res