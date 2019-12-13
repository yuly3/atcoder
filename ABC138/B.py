def solve():
    N, *al = map(int, open(0).read().split())

    ans = 1 / sum(map(lambda x: 1 / x, al))

    print(ans)


if __name__ == '__main__':
    solve()
