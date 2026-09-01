class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        mergedArray = nums1 + nums2
        mergedArray.sort()

        totalLength = len(mergedArray)
        if totalLength % 2 == 0:
            return(mergedArray[totalLength // 2 - 1] 
            + mergedArray[totalLength // 2]) / 2.0

        else:
            return mergedArray[totalLength // 2]
        