# braces matches
def is_valid_braces(values):
    stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
    for pVal in values:
        if pVal in pchar:
            stack.append(pVal)
        elif len(stack) == 0 or pchar[stack.pop()] != pVal:
            return False
    return len(stack) == 0
def braces_list_check(values):
    i = 1
    while i < values.__len__():
        if is_valid_braces(values[i]):
            print('YES')
        else:
            print('NO')
        i = i+1