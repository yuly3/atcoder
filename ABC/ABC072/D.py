def solve():
    N = int(input())
    p = list(map(int, input().split()))
    
    ans = 0
    for i in range(N - 1):
        if i + 1 == p[i]:
            p[i], p[i + 1] = p[i + 1], p[i]
            ans += 1
    if p[N - 1] == N:
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
