class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: #check if temp is higher than top 
                stackT, stackInd = stack.pop() #pop if we find higher temp
                res[stackInd] = i - stackInd #calculate the distance
            stack.append((t, i))
        return res


