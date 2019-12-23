def solve():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    A = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        A[i] = list(map(int, input().split()))

    ans = 0
    for i in range(N):
        t = 0
        for a, b in zip(A[i], B):
            t += a * b
        if 0 < t + C:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
