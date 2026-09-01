class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest_streak=1
        current_streak=1

        for i in range(len(nums)):
            if(nums[i]==nums[i-1]+1):
                current_streak +=1
            elif nums[i]==nums[i-1]:
                continue
            else:
                longest_streak=max(longest_streak, current_streak)
                current_streak=1
        return max(longest_streak, current_streak)

