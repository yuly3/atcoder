def solve():
    N, T = map(int, input().split())
    c, t = [0] * N, [0] * N
    for i in range(N):
        c[i], t[i] = map(int, input().split())

    ans = 2000
    for i in range(N):
        if t[i] <= T:
            ans = min(ans, c[i])
    if ans == 2000:
        print('TLE')
    else:
        print(ans)


if __name__ == '__main__':
    solve()
