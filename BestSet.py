# 2,9 -> { 1, 8 }, { 2, 7 }, { 3, 6 }, { 4, 5 } => {4,5}
# 2,1 => [-1]
def best_set(n,s):
    # 1
    # if n > s:
    #     return [-1]
    # answer = []
    # avg = s // n
    # for i in range(n):
    #     answer.append(avg)
    # em = s - avg * n
    # while em > 0:
    #     for i in range(n):
    #         if em > 0:
    #             answer[i] += 1
    #             em -= 1
    #         else:
    #             break
    # return sorted(answer)

    # 2
    # hint: (n-s % n) -> '%' operation first than '-' operation
    # return [s // n] * (n - (s % n)) + [s // n + 1] * (s % n) if n <= s else [-1]

    # 3
    answer = [s // n] * n
    if s < n:
        return [-1]
    else:
        for i in range(s % n):
            answer[i] += 1
        answer.sort()
        return answer