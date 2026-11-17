class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count the numbers seen in nums
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        #empty freq list
        freq = []
        for i in range(len(nums) + 1):
            freq.append([])
        #put the count into the freq list
        for n, c in count.items():
            freq[c].append(n)
        #
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        