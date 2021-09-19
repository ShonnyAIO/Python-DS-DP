def isValid(self, s):
    if not s:
        return True
    a=['(','{','[']
    b=[')','}',']']
    stack=[s[0]]
    for i in range(1,len(s)):
        if s[i] in a:
            stack.append(s[i])
        elif not stack:
            return False
        elif stack.pop()!=a[b.index(s[i])]:
            return False
    return True if not stack else False