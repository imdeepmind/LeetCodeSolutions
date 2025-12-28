class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pivot = strs[0]
        output = ""

        for c in pivot:
            delta = output + c
            is_match = True

            for word in strs[1:]:
                if is_match and not word.startswith(delta):
                    is_match = False
            
            if is_match:
                output = delta
            else:
                break
            
        return output
            

