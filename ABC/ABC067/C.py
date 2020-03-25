def solve():
    N = int(input())
    a = list(map(int, input().split()))
    
    cumsum = [0] * (N + 1)
    for i in range(N):
        cumsum[i + 1] = cumsum[i] + a[i]
    
    ans = 10 ** 10
    for i in range(1, N):
        ans = min(ans, abs(cumsum[i] - (cumsum[N] - cumsum[i])))
    print(ans)


if __name__ == '__main__':
    solve()
