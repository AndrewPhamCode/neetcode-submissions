class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 
                #check the leftside
            elif nums[l] <= nums[m]:
                #checks to see if its in the bounds of the left
                if nums[l] <= target <= nums[m]:
                    r = m - 1 # close in the binary search to the left 
                else:
                    l = m + 1
            else: #check the right side 
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

