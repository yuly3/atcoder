def solve():
    BTC = 380000
    N = int(input())
    
    ans = 0
    for _ in range(N):
        x, u = map(str, input().split())
        x = float(x)
        if u == 'JPY':
            ans += x
        else:
            ans += x * BTC
    print(ans)


if __name__ == '__main__':
    solve()
