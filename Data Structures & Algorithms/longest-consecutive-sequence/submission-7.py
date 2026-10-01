class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: #set the default length to 1
                length = 1
                while (num + length) in numSet: #check if next number in hashset
                    length += 1
                longest = max(length, longest) #update the longest 
        return longest