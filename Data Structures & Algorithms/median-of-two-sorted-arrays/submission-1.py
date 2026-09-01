class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        mergedArray = nums1 + nums2
        mergedArray.sort() #Sort the two arrays

        totalLength = len(mergedArray)
        if totalLength % 2 == 0: #If the array is even add the two middle values and divide by two
            return(mergedArray[totalLength // 2 - 1] 
            + mergedArray[totalLength // 2]) / 2.0

        else:
            return mergedArray[totalLength // 2] #return the middle index if it's even
        