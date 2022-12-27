class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        idx1, idx2 = 0, 0
        smallest = float('inf')
        index = []
        
        
        while idx1 < len(arr) and idx2 < len(arr):
            if idx1 != idx2:
                first, second = arr[idx1], arr[idx2]
                
                if first > second:
                    current = first - second
                    idx2 += 1
                elif first < second:
                    current = second - first
                    idx1 += 1
                else:
                    index.append([first, second])
                    smallest = 0
                    idx2 += 1
                
                if smallest > current:
                    smallest = current
                    index = [[first, second]]
                elif smallest == current:
                    index.append([first, second])
                    
            else:
                idx2 += 1
        
        return index
