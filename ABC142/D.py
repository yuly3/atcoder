def factrization(n):
    arr = set()
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.add(i)

    if temp != 1:
        arr.add(temp)

    if arr == []:
        arr.add(n)

    return arr


def solve():
    A, B = map(int, input().split())

    a_arr = factrization(A)
    b_arr = factrization(B)

    s_ans = a_arr & b_arr
    print(len(s_ans) + 1)


if __name__ == '__main__':
    solve()
