class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        CloseToOpen = {
            ')':'(', "}":'{', ']':'['
        }
        for char in s:
            if char in CloseToOpen.values():
                stack.append(char)
            elif char in CloseToOpen:
                if not stack or stack[-1] != CloseToOpen[char]:
                    return False
                stack.pop()
        return len(stack) == 0