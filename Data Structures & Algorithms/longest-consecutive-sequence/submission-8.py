class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #make a hashtable to define all numbers seen
        #increment by 1 from the value in the hashset, stores in buckets 
        #count the current streak and return the max one 
        #check if num - 1 in set

        if not nums:
            return 0 
        res = 0 
        nums.sort()

        curr, streak = nums[0], 0
        i = 0
        while i < len(nums):
            if curr != nums[i]:
                curr = nums[i]
                streak = 0
            while i < len(nums) and nums[i] == curr:
                i += 1
            streak += 1
            curr += 1
            res = max(res, streak)
        return res


        