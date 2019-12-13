def solve():
    N, K, *hl = map(int, open(0).read().split())
    ans = 0

    for i in hl:
        if i >= K:
            ans += 1

    print(ans)


if __name__ == '__main__':
    solve()
