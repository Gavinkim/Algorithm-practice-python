# find same name in name list (linear search)
def find_same_name(name_list):
    name_list_len = len(name_list)
    same_name_result = set()
    for i in range(0, name_list_len - 1):
        for j in range(i + 1, name_list_len):
            # print('compare {} and {}'.format(name_list[i],name_list[j]))
            if name_list[i] == name_list[j]:
                same_name_result.add(name_list[i])
    return same_name_result

# using dictionary
def find_same_name_use_dic(name_list):
    name_dict = {}
    for name in name_list:
        if name in name_dict: # if find same name then increment value
            name_dict[name] += 1
        else:
            name_dict[name] = 1
    result = set()
    # if find value >=2 then add to result
    for name in name_dict:
        if name_dict[name] >= 2:
            result.add(name)
    return result

# 'abcde' -> 'c'
# 'qwer' -> 'we'
def find_middle_word(words):
    # 1
    #     words_len = len(words)
    #     mid = words_len//2
    #     if words_len % 2 == 0:
    #         return words[mid-1:mid+1]
    #     else:
    #         return words[mid]

    # 2
    return words[(len(words) - 1)//2:len(words)//2+1]

# "1234" -> 1234
# "-1234" -> -1234
def strToInt(str):
    # 1
    # return int(str)

    # 2
    result = 0
    if ord(str[0]) > 48:
        num = -1
        for i in str:
            result += (ord(str[num]) - 48) * pow(10, abs(num + 1))
            num -= 1
    else:
        result = -strToInt(str[1:])
    return result