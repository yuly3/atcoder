def solve():
    A, B, C, X, Y = map(int, input().split())
    
    ans = 5000 * 2 * 10 ** 5
    for i in range(max(X, Y) + 1):
        ans = min(ans, 2 * i * C + A * max(0, X - i) + B * max(0, Y - i))
    print(ans)


if __name__ == '__main__':
    solve()
