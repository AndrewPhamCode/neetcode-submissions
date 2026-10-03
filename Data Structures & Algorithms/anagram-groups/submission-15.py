class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs: #iterate through each word in strs
            count = [0] * 26 #stores each letter 
            for c in s:
                count[ord(c) - ord('a')] += 1 #increments each time a letter is seen
            res[tuple(count)].append(s)
        return list(res.values())
