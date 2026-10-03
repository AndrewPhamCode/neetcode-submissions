class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #define the prefix array 
        #define the suffix array 

        #calculate the product by combining the prefix and suffix array 
        #initalize everything as zeroes 
        n = len(nums)
        #result starts as 1 
        res = [1] * n 

        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res

        

        




        
