class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []

        for index, c in enumerate(code):
            if k == 0:
                res.append(0)
            elif k > 0:
                alpha = code[index+1: index+k+1]

                if len(alpha) != k:
                    delta = k - len(alpha)
                    alpha += code[0:delta]

                res.append(sum(alpha))
            else:
                alpha = code[max(0, index+k):index]
                
                if len(alpha) != -1 * k:
                    delta = len(alpha) + k
                    alpha += code[delta:]

                res.append(sum(alpha))

        return res

            