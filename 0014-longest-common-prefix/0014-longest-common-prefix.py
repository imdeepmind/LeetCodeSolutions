class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        pivot = strs[0]

        for anchor in pivot:
            matched = True
            for word in strs[1:]:
                if not word.startswith(res + anchor):
                    matched = False

            if matched:
                res += anchor
            else:
                break

        return res