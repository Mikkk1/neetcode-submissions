class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        out = sorted(dic, key= lambda x: dic[x], reverse= True)
        list(out)
        return out[:k]
