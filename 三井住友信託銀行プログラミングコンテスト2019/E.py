def solve():
    MOD = 1000000007
    N, *a_l = map(int, open(0).read().split())
    t_l = [3] + [0 for _ in range(N+1)]
    ans = 1

    for a in a_l:
        ans = t_l[a] * ans % MOD
        t_l[a] -= 1
        t_l[a+1] += 1

    print(ans)


if __name__ == '__main__':
    solve()