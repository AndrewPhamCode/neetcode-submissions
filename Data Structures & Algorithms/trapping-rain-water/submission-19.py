class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        rain = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(height[l], leftMax)
                rain += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(height[r], rightMax)
                rain += rightMax - height[r]
        return rain
        