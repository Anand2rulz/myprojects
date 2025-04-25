class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        b={"(":")","{":"}","[":"]"}
        for i in s:
            if stack and stack[-1]==i:
                stack.pop()
                continue
            if i in b.keys():
                stack.append(b[i])
            elif i in b.values():
                return False
        return len(stack)==0
