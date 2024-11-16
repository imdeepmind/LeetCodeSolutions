class Solution:
    def trap(self, height: List[int]) -> int:
        left_maxes = []
        left_max = 0

        for i in range(len(height)):
            if i == 0:
                left_maxes.append(0)
                continue

            if height[i-1] > left_max:
                left_max = height[i-1]
                left_maxes.append(height[i-1])
            else:
                left_maxes.append(left_max)

        right_maxes = []
        right_max = 0

        for i in range(len(height)-1, -1, -1):
            if i == len(height) - 1:
                right_maxes.append(0)
                continue

            if height[i+1] > right_max:
                right_max = height[i+1]
                right_maxes.append(height[i+1])
            else:
                right_maxes.append(right_max)

        right_maxes = right_maxes[::-1]

        area = 0
        for i in range(len(height)):
            area += max(0, min(left_maxes[i], right_maxes[i]) - height[i])

        return area