class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, j in enumerate(nums):
            compliment = target - j
            if compliment in dic:
                return [dic[compliment], i]
            else:
                dic[j] = i