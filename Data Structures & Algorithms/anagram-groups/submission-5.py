class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #dict where each key automatically starts with an empty list
        for s in strs:
            sortedS = ''.join(sorted(s)) #sorted list of characters put back together
            res[sortedS].append(s) #add the original word into group
        return list(res.values())