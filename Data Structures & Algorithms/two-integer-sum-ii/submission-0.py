class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L <= R:
            if target != (numbers[L] + numbers[R]):
                if target > (numbers[L] + numbers[R]):
                    L += 1
                else:
                    R -= 1
            else:
                return [L+1, R+1]