class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        resp = ""

        while columnNumber > 0:
            if columnNumber <= 26:
                resp += chr(columnNumber+64)
                break
            
            columnNumber -= 1
            resp += chr(columnNumber%26+65)
            columnNumber //= 26

        return resp[::-1]
