from bisect import bisect_left

N, M, *A = map(int, open(0).read().split())
A.sort()


def calc(t):
    cnt = 0
    for ai in A:
        cnt += N - bisect_left(A, t - ai)
    if M <= cnt:
        return True
    else:
        return False


def solve():
    left, right = 0, 2 * 10 ** 5 + 1
    while 1 < right - left:
        mid = (left + right) // 2
        if calc(mid):
            left = mid
        else:
            right = mid
    
    sum_A = [0] * N
    sum_A[-1] = A[-1]
    for i in range(N - 2, -1, -1):
        sum_A[i] = sum_A[i + 1] + A[i]
    
    ans = 0
    add_cnt = 0
    for ai in A:
        index = bisect_left(A, left - ai)
        if index == N:
            continue
        add_cnt += N - index
        ans += (N - index) * ai + sum_A[index]
    ans -= left * (add_cnt - M)
    print(ans)


if __name__ == '__main__':
    solve()
