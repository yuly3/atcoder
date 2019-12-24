def solve():
    N, *p = map(int, open(0).read().split())
    ans = max(p) // 2 + sum(p) - max(p)
    print(ans)


if __name__ == '__main__':
    solve()
