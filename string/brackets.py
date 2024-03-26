class Solution:
    def isbalanced(self, string: str):
        stack = []
        opening = {"(": ")", "{": "}", "[": "]"}
        for index, char in enumerate(string, start=1):
            if char in opening:
                stack.append((char, index))
            elif char in opening.values():
                if not stack:
                    return index
                top, _ = stack.pop()
                if opening[top] != char:
                    return index
        return "Success" if not stack else stack.pop()[1]
