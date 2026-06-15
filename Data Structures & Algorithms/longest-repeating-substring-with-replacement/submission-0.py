class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        L = 0
        maxLength = 0
        dic = {}
        for R in range(len(s)):
            dic[s[R]] = dic.get(s[R],0) + 1
            if  (R - L + 1) - max(dic.values()) > k:
                dic[s[L]] -= 1
                L += 1
            maxLength = max(maxLength, (R - L +1))
        return maxLength
            