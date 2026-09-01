class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #dict to store how many times each number appears
        
        for num in nums:
            count[num] = 1 + count.get(num, 0) #if num is already in count add 1 to its current count

        arr = [] #stores pairs [frequency, number]
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort() #sort from smallest frequency to largest frequency

        res = [] #final answer

        #takes number with highest freq
        #arr.pop removes the last item which is the highest frequency
        while len(res) < k:
            res.append(arr.pop()[1]) 
        return res