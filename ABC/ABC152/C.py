def solve():
    N, *P = map(int, open(0).read().split())
    
    ans = 0
    tmp = 10 ** 6
    for i in range(N):
        tmp = min(tmp, P[i])
        if P[i] <= tmp:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
