class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            if c == ")" or c == "}" or c == "]":
                    
                if len(stack) > 0:
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
        if len(stack) == 0:
            return True
        else:
            return False