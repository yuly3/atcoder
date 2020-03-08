def solve():
    n, *p_l = map(int, open(0).read().split())
    ans = 0

    for i in range(1, n-1):
        if p_l[i-1] < p_l[i] < p_l[i+1] or p_l[i+1] < p_l[i] < p_l[i-1]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()