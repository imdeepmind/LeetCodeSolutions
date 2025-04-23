class Solution:
    def trap(self, height: List[int]) -> int:
        left_pillars = []
        right_pillars = []

        left_max = float('-inf')
        right_max = float('-inf')

        for i in range(len(height)):
            if i == 0:
                left_pillars.append(0)
                left_max = height[i]
                continue
            
            left_max = max(height[i-1], left_max)
            left_pillars.append(left_max)
        
        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                right_pillars.append(0)
                right_max = height[i]
                continue
            
            right_max = max(right_max, height[i+1])
            right_pillars.append(right_max)

        right_pillars = right_pillars[::-1]

        area = 0

        for i in range(len(height)):
            area += max(0, min(left_pillars[i], right_pillars[i]) - height[i])

        return area

