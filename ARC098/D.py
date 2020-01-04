from itertools import accumulate


def solve():
    N, *A = map(int, open(0).read().split())
    
    ans, l = 0, 0
    sum_lr, xor, length = 0, 0, 0
    for r in range(N):
        sum_lr += A[r]
        xor ^= A[r]
        length += 1
        while sum_lr != xor:
            sum_lr -= A[l]
            xor ^= A[l]
            l += 1
            length -= 1
        ans += length
    print(ans)


if __name__ == '__main__':
    solve()
