def solve():
    N, K, *x = map(int, open(0).read().split())
    
    ans = 10 ** 9
    for l in range(N - K + 1):
        r = l + K - 1
        ans = min(ans, abs(x[l]) + abs(x[r] - x[l]), abs(x[r]) + abs(x[r] - x[l]))
    print(ans)


if __name__ == '__main__':
    solve()
