class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countT, countS = {}, {} #create 2 hashtables for the 2 strings
        for i in range(len(s)): 
            #frequency counter for all 26 letters of both strings 
            countT[t[i]] = 1 + countT.get(t[i], 0) 
            countS[s[i]] = 1 + countS.get(s[i], 0)
        return countS == countT
