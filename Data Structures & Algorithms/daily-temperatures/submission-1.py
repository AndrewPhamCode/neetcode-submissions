class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = []

        for i in range(n): #starting day loop
            count = 1 #count how many days until warmer
            j = i + 1 #check the day after current day
            while j < n: #keep searching until loop ends
                if temperatures[j] > temperatures[i]: #if next day is warmer stop searching
                    break
                j += 1 #otherwise keep incrementing and increase count
                count += 1
            count = 0 if j == n else count #no warmer day
            res.append(count) #store the result
        return res