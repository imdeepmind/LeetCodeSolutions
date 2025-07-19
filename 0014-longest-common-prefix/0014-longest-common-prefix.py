class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]

        resp = ""

        for c in pivot:
            is_match = True
            for word in strs[1:]:
                if not word.startswith(resp + c):
                    is_match = False
                
            if is_match:
                resp += c
            else:
                break
            
        return resp