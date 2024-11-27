class Solution:
    def performOperation(self, val1, val2, operation):
        val1, val2 = int(val1), int(val2)

        if operation == '+':
            return val1 + val2
        
        if operation == '-':
            return val1 - val2
        
        if operation == '*':
            return val1 * val2
        
        if operation == '/':
            return int(float(val1) / val2)

    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > i:
            if tokens[i] not in ('+', '-', '*', '/'):
                i += 1
                continue
            
            a, b = tokens[i-2], tokens[i-1]
            operation = tokens[i]

            del tokens[i-2]
            del tokens[i-2]
            del tokens[i-2]
            
            tokens.insert(i-2, self.performOperation(a, b, operation))
            i = 0
        
        return int(tokens[0])