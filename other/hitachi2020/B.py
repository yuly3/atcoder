def solve():
    A, B, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    x, y, c = [0] * M, [0] * M, [0] * M
    for i in range(M):
        x[i], y[i], c[i] = map(int, input().split())
    
    ans = min(a) + min(b)
    for i in range(M):
        ans = min(ans, a[x[i] - 1] + b[y[i] - 1] - c[i])
    print(ans)


if __name__ == '__main__':
    solve()
