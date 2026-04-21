class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            if c == ")" or c == "}" or c == "]":
                    
                if stack:
                    if c == ")":
                        if stack.pop() != "(":
                            return False
                    if c == "}":
                        if stack.pop() != "{":
                            return False
                    if c == "]":
                        if stack.pop() != "[":
                            return False
                else:
                    return False

        return len(stack) == 0