import random


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


# find number position (linear search)
def find_target_num_pos(num_list, target_num):
    num_list_len = len(num_list)
    for pos in range(0, num_list_len):
        if target_num == num_list[pos]:
            return pos
    return -1  # if not found number position return -1


# binary search in sorted number list
def binary_search_target_num_pos(sorted_num_list, target_num):
    start = 0
    end = len(sorted_num_list) - 1
    while start <= end:
        mid = (start + end) // 2  # 4/2=2.0, 4//2 = 2
        # print('mid: {}'.format(mid))
        if target_num == sorted_num_list[mid]:
            return mid
        elif target_num > sorted_num_list[mid]:
            start = mid + 1  # keep going right
        else:
            end = mid - 1  # keep going left
    return -1  # not found


# recurecive factorial number
def recursive_factorial(num):
    if num <= 1:  # end condition
        return 1
    # print('{} * recursive_factorial({})'.format(num,num-1))
    return num * recursive_factorial(num - 1)


# find gcd
def find_gcd(num1, num2):
    find_result = min(num1, num2)
    while True:
        if num1 % find_result == 0 and num2 % find_result == 0:
            return find_result
        find_result = find_result - 1


# find gcd using euclidean
def find_euclidean_gcd(num1, num2):
    # print("find_euclidean_gcd: {} and {}".format(num1,num2))
    if num2 == 0:
        return num1
    return find_euclidean_gcd(num2, num1 % num2)


# find min position
def find_min_pos(num_list):
    num_list_len = len(num_list)
    min_pos = 0
    for pos in range(1, num_list_len):
        if num_list[pos] < num_list[min_pos]:
            min_pos = pos
    return min_pos


# find max position
def find_max_pos(num_list):
    num_list_len = len(num_list)
    max_pos = 0
    for pos in range(1, num_list_len):
        if num_list[pos] > num_list[max_pos]:
            max_pos = pos
    return max_pos


# bubble sorting
def bubble_sort(num_list):
    num_list_len = len(num_list)
    for i in range(num_list_len-1, 0, -1):  # step: -1 , from num_list_len -1 to 0
        for j in range(i):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
    return num_list


# selection sort
def selection_sort_list(num_list):
    num_list_len = len(num_list)
    for current_pos in range(0, num_list_len - 1):
        min_pos = current_pos
        for next_pos in range(current_pos + 1, num_list_len):
            if num_list[next_pos] < num_list[min_pos]:
                min_pos = next_pos
        num_list[current_pos], num_list[min_pos] = num_list[min_pos], num_list[current_pos]  # swap
    return num_list


# insert sorting
def insert_sort_list(num_list):
    num_list_len = len(num_list)
    for current_pos in range(1, num_list_len):
       pos_val = num_list[current_pos]
       prev_pos = current_pos - 1
       while prev_pos >= 0 and num_list[prev_pos] > pos_val:
           num_list[prev_pos + 1] = num_list[prev_pos] # keep going right for insert space
           prev_pos -= 1
       num_list[prev_pos + 1] = pos_val # save pos_val to find position
    return num_list


# merge sorting
def merge_sort(num_list):
    num_list_len = len(num_list)
    if num_list_len <= 1:
        return num_list
    mid = num_list_len//2
    # sorted two list => left_list and right_list
    left_list = merge_sort(num_list[:mid])
    right_list = merge_sort(num_list[mid:])
    i,j,k = 0,0,0
    while i<len(left_list) and j<len(right_list):
        # compare left list and right list and add to list
        if left_list[i] < right_list[j]:
            num_list[k] = left_list[i]
            i += 1
        else:
            num_list[k] = right_list[j]
            j += 1
        k += 1
    if i == len(left_list):  # if left_list full and remain right_list?
        while j<len(right_list):
            num_list[k] = right_list[j]
            j += 1
            k += 1
    elif j == len(right_list):  # if right_list full and remain right_list?
        while i<len(left_list):
            num_list[k] = left_list[i]
            i += 1
            k += 1
    return num_list


# quick sorting
def quick_sort(num_list):
    num_list_len = len(num_list)
    if num_list_len <=1:
        return num_list
    pivot = num_list[-1]
    smaller_list = []
    bigger_list = []
    for i in range(0, num_list_len-1):
        if num_list[i] < pivot:
            smaller_list.append(num_list[i])
        else:
            bigger_list.append(num_list[i])
    # add lists (smaller_list and pivot,bigger_list) and recursive 
    # [1,2] + [3] + [4,5] => [1,2,3,4,5]    
    return quick_sort(smaller_list) + [pivot] + quick_sort(bigger_list)


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


# find maze
def find_maze(maze, start, end):
    remain_queue = []
    added_pos_set = set()
    remain_queue.append(start)
    added_pos_set.add(start)
    while remain_queue:
        p = remain_queue.pop(0)
        v = p[-1]
        if v == end:
            return p
        for x in maze[v]:
            if x not in added_pos_set:
                remain_queue.append(p+' => '+x)
                added_pos_set.add(x)
    return "Not found ways"


# find middle character in word (if word length  even then middle two word)
def find_middle_word(words):
    return words[(len(words) - 1)//2:len(words)//2+1]

# def find_middle_word(words):
#     words_len = len(words)
#     mid = words_len//2
#     if words_len % 2 == 0:
#         return words[mid-1:mid+1]
#     else:
#         return words[mid]


# main function
if __name__ == '__main__':
    num_list = [random.randint(1,100) for _ in range(10)]
    sorted_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    name_list = ["Tome", "Gavin", "James", "Worse", "Tome", "Jack", "Gavin"]
    maze = {
        'a': ['e'],
        'b': ['c', 'f'],
        'c': ['b', 'd'],
        'd': ['c'],
        'e': ['a', 'i'],
        'f': ['b', 'g', 'j'],
        'g': ['f', 'h'],
        'h': ['g', 'l'],
        'i': ['e', 'm'],
        'j': ['n', 'f', 'k'],
        'k': ['j', 'o'],
        'l': ['h', 'p'],
        'm': ['i', 'n'],
        'n': ['m', 'j'],
        'o': ['k'],
        'p': ['l']
    }
    # print('find same name: {}'.format(find_same_name(name_list)))
    # print('find same name using dict: {}'.format(find_same_name_use_dic(name_list)))
    # print('factorial: {}'.format(recursive_factorial(10)))
    # print('gcd: {}'.format(find_gcd(60,24)))
    # print('euclidean gcd: {}'.format(find_euclidean_gcd(60,24)))
    # print('find target num position: {}'.format(find_target_num_pos(num_list,111)))
    # print('find min pos in number list: {}'.format(find_min_pos(num_list)))
    # print('find max pos in number list: {}'.format(find_max_pos(num_list)))
    # print('binary search: {}'.format(binary_search_target_num_pos(sorted_num_list,10)))
    # print('select sorted:{}'.format(selection_sort_list(num_list)))
    # print('bubble sorting: {}'.format(bubble_sort(num_list)))
    # print('insert sorted: {}'.format(insert_sort_list(num_list)))
    # print('ferma test: {}'.format(prime_number_ferma_test(113)))
    # print('check prime number: {}'.format(check_prime_number(113)))
    # print('merge sorting: {}'.format(merge_sort(num_list)))
    # print('palindrome: {}'.format(check_palindrome("hellolleh")))
    # print('quick sorting: {}'.format(quick_sort(num_list)))
    # print(find_maze(maze, "a", "p"))
    # print(find_middle_word('abcde'))
    print(longest_palindrome('abacca'))
