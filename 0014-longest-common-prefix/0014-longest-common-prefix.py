class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        resp = ""
        
        for c in pivot:
            delta = resp + c
            is_match = True

            for word in strs[1:]:
                if is_match and not word.startswith(delta):
                    is_match = False
                
            if is_match:
                resp = delta
            else:
                break
        
        return resp