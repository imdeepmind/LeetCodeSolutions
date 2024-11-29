class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for r in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[r]:
                temp, idx = stack.pop()
                res[idx] = r - idx

            stack.append((temperatures[r], r))
        
        return res


