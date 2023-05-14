class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        tri = []
        
        for i in range(1, rowIndex+2):
            row = []
            for j in range(1, i+1):
                if i > 1:
                    if j in (1, i):
                        row.append(1)
                    else:
                        row.append(tri[i-2][j-2] + tri[i-2][j-1])
                else:
                    row.append(1)
            
            tri.append(row)
        
        return tri[-1]
