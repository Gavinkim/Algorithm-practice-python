# recursive factorial number
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

# two matrix multiply
# A = [[1,2],[2,3]]
# B = [[3,4],[5,6]]
def multiply_matrix(A, B):
    # 1
    # return [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]

    # 2
    result = []
    b_len = len(B)
    for i in range(len(A)):
        result.append([])
        for j in range(len(B[0])):
            result[i].append(sum(A[i][k] * B[k][j] for k in range(b_len)))
    return result