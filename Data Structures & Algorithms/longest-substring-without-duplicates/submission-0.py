class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            hashSet = set()
            for j in range(i , len(s)):
                if s[j] in hashSet:
                    break
                hashSet.add(s[j])
            result = max(result, len(hashSet))
        return result


        