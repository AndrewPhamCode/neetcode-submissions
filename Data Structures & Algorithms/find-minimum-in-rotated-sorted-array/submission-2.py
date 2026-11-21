class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 
        #3, 4, 5, 6, 1, 2

        while l < r:
            m = (l + r) // 2
            if nums[m] < nums[r]:
                r = m 
            else:
                l = m + 1
        return nums[l]

