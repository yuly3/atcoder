def solve():
    N, *dl = map(int, open(0).read().split())
    ans = 0

    for i in range(N - 1):
        for j in range(i + 1, N):
            ans += dl[i] * dl[j]

    print(ans)


if __name__ == '__main__':
    solve()
