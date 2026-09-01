class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0
        left = 0 
        right = len(height) - 1

        leftMax = height[left]
        rightMax = height[right]
        rainSum = 0
        
        while left < right:
            if leftMax < rightMax:
                left += 1
                leftMax = max(leftMax, height[left])
                rainSum += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                rainSum += rightMax - height[right]

        return rainSum
        
        