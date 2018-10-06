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