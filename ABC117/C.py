def solve():
    N, M, *X = map(int, open(0).read().split())
    
    X.sort()
    dx = [0 for _ in range(M - 1)]
    for i in range(1, M):
        dx[i - 1] = X[i] - X[i - 1]
    
    dx.sort()
    ans = 0
    for i in range(M - N):
        ans += dx[i]
    print(ans)


if __name__ == '__main__':
    solve()
