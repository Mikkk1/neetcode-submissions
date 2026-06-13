class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        running = 1
        left = [1] * len(nums)
        right = [1] * len(nums)
        for i in range(len(nums)):
            left[i] = running
            running = running * nums[i]
        running = 1
        for i in range(len(nums) -1, -1, -1):
            right[i] = running
            running = running * nums[i]
        output = [left[i] * right[i] for i in range(len(nums))]
        return output