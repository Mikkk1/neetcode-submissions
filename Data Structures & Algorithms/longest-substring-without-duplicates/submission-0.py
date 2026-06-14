class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        MaxLength = 0
        L = 0
        charSet = set()
        for R in range(len(s)):
            if s[R] in charSet:
                while s[R] in charSet:
                    charSet.remove(s[L])
                    L+=1
                charSet.add(s[R])
                MaxLength = max(MaxLength, R - L + 1)
            else:
                charSet.add(s[R])
                MaxLength = max(MaxLength, R - L + 1)

        return MaxLength

