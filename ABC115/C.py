def solve():
    N, K, *h = map(int, open(0).read().split())
    h.sort(reverse=True)
    
    ans = 10 ** 9
    for i in range(N - K + 1):
        ans = min(ans, h[i] - h[i + K - 1])
    print(ans)


if __name__ == '__main__':
    solve()
