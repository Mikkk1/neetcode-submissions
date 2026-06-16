import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)
        result = max(piles)
        while L<= R:
            mid = (L+R)//2
            hours_taken = sum(math.ceil(p/mid) for p in piles)
            if hours_taken <= h:
                result = min(result, mid)
                R = mid - 1
            else:
                L = mid + 1
        return result