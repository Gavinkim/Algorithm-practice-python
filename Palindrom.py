# palindrome
def check_palindrome(words):
    str_queue = []
    str_stack = []
    for str in words:
        if str.isalpha():  # ignore space, number, special character
            str_queue.append(str.lower())
            str_stack.append(str.lower())
    while str_queue:
        if str_queue.pop(0) != str_stack.pop():
            return False
    return True


# longest palindrome (abacca)
# result -> acca
def longest_palindrome(s):
    # 1
    # return len(s) if s[::-1] == s else max(longest_palindrome(s[:-1]), longest_palindrome(s[1:]))
    # ====================================
    # 2
    # for i in range(len(s), 0, -1):
    #     for j in range(len(s) - i + 1):
    #         print(i, j, s[j:j + i], s[j:j + i][::-1])
    #         if s[j:j + i] == s[j:j + i][::-1]:  # s[j:j+i][::-1] -> s[j:j+i] to reverse
    #             return i
    # ====================================
    # 3
    results = []
    for i in range(len(s)):
        for j in range(0, i):
            substr = s[j:i + 1]
            if substr == substr[::-1]:  # compare substr and substr reverse
                results.append(substr)
    return len(max(results, key=len))