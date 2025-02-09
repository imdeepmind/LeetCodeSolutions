from collections import defaultdict

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        notes = defaultdict(int)

        for bill in bills:
            notes[bill] += 1
            
            if bill == 10:
                if notes[5] > 0:
                    notes[5] -= 1
                else:
                    return False
            
            if bill == 20:
                remaining = 15
                if notes[10] > 0:
                    notes[10] -= 1
                    remaining -= 10
                
                if notes[5] >= (remaining // 5):
                    notes[5] -= (remaining // 5)
                else:
                    return False
            
        return True

                    
                    