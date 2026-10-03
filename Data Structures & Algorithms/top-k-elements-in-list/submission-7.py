class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        #define a hashmap to store frequency of each number
        
        #iterate through the array and incrememnt if num is seen
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        while len(res) < k:
            res.append(arr.pop()[1])
        return res


        #sort the array from most seen to least 
        #return as an array