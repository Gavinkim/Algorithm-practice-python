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