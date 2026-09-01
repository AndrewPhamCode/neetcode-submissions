class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures) #default answer is 0
        stack = [] #pair: [temp, index]

        for i, t in enumerate(temperatures): 
            #i is current index, t is temperature on that day
            while stack and t > stack[-1][0]: 
                #as long as today is warmer than top of stack
                stackT, stackInd = stack.pop() 
                #pop the previous colder day
                res[stackInd] = i - stackInd
                #number of days waited = current index - prevous index
            stack.append((t, i))
            #push current day onto stack
        return res