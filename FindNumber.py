# find number position (linear search)
def find_target_num_pos(num_list, target_num):
    num_list_len = len(num_list)
    for pos in range(0, num_list_len):
        if target_num == num_list[pos]:
            return pos
    return -1  # if not found number position return -1

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

# remove_sequence_duplicated_number
# arr = [1, 1, 3, 3, 0, 1, 1] -> [1, 3, 0, 1]
# arr = [4, 4, 4, 3, 3] -> [4, 3]
def remove_sequence_duplicated_number(arr):
    # 1
    # result = []
    # for c in arr:
    #     if (len(result) == 0) or (result[-1] != c):
    #         result.append(c)
    # return result

    # 2
    return [v for i, v in enumerate(arr) if i == 0 or v != arr[i - 1]]

    # 3
    # s_list = list()
    # s_list.append(arr[0])
    # for i in range(len(arr)):
    #     if arr[i] == arr[i - 1]:
    #         continue
    #     s_list.append(arr[i])
    # return s_list

    # 4
    # a = []
    # for i in arr:
    #     if a[-1:] == [i]:
    #         continue
    #     a.append(i)
    # return a

    # 5
    # result = []
    # for i in range(len(arr)):
    #     if arr[i - 1] == arr[i]:
    #         continue
    #     else:
    #         result += arr[i]
    # return result