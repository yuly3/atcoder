def solve():
    N, *A = map(int, open(0).read().split())

    B = [0] * N
    for i, a in enumerate(A):
        B[i] = a - (i + 1)
    B.sort()

    if N % 2 == 1:
        b = B[N // 2]
    else:
        b = (B[N // 2] + B[N // 2 - 1]) // 2

    ans = 0
    for i, a in enumerate(A):
        ans += abs(a - (b + i + 1))
    print(ans)


if __name__ == '__main__':
    solve()
