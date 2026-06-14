class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        L = 0
        R = len(heights) - 1
        while L < R:
            maxAmount = max(maxAmount, min(heights[L], heights[R]) * (R - L))
            if heights[L] < heights[R]:
                L+=1
            elif heights[L] > heights[R]:
                R-=1
            else:
                L+=1
        return maxAmount