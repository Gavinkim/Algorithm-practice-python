# cesar cryptography
# AB,1 -> BC
# z,1 -> a
# Abrzz,2 -> Cdtbb
# hint: chr(x) -> chr(65 => 'A'
# hint: ord(x) -> ord('A') => 65
def cesar(s, n):
    # 1
    # lower = 'abcdefghijklmnopqrstuvwxyz'
    # upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # res = ''
    # for c in s:
    #     if c in lower:
    #         res += lower[(lower.index(c) + n) % 26]
    #     elif c in upper:
    #         res += upper[(upper.index(c) + n) % 26]
    #     else:
    #         res += c
    # return res

    # 2
    result = ""
    for k in s:
        if k.isalpha():
            if k.islower():
                result += chr((ord(k) - ord("a") + n) % 26 + ord("a"))
            else:
                result += chr((ord(k) - ord("A") + n) % 26 + ord("A"))
        else:
            result += k
    return result