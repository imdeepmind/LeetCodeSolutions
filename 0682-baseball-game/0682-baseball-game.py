class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = []

        for operation in operations:
            match(operation):
                case 'C':
                    if res:
                        del res[-1]
                case 'D':
                    if res:
                        res.append(2 * res[-1])
                case '+':
                    if res and len(res) >= 2:
                        res.append(res[-1] + res[-2])
                case _:
                    res.append(int(operation))
        
        return sum(res)