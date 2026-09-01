class Solution:
    def findMin(self, nums: List[int]) -> int:
        currentMin = nums[0]
        for i in nums:
            if i < currentMin:
                currentMin = i
        return currentMin