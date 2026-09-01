class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        rain = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                rain += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                rain += rightMax - height[r]
        return rain
            
