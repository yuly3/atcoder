def solve():
    N, L = map(int, input().split())
    tastes = [i for i in range(L, L+N)]
    ans = sum(tastes) - min(tastes, key=abs)
    print(ans)


if __name__ == '__main__':
    solve()