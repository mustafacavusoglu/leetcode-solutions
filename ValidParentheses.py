def isValid(s: str) -> bool:
    state = False

    while len(s) > 0:
        l = len(s)
        s = s.replace("()", "").replace("{}", "").replace("[]","")
        if l == len(s):
            return state
    return not state


print(isValid("()[]{}"))