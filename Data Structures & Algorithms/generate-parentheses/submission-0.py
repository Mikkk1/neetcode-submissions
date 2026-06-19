class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(OC, CC, current):
            if OC == n and CC == n:
                result.append(current)
            if OC < n:
                backtrack(OC + 1, CC, current + "(")
            if CC < OC:
                backtrack(OC, CC + 1, current + ")")
        backtrack(0,0,"")
        return result