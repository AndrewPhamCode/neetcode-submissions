class Solution:
    def isValid(self, s: str) -> bool:
        #create a dictionary to check for bracket 
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

