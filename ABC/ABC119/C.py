N, A, B, C, *l = map(int, open(0).read().split())
ans = 10 ** 9


def dfs(a, b, c, cur, cost):
    if cur == N:
        if not a or not b or not c:
            return
        global ans
        ans = min(ans, abs(a - A) + abs(b - B) + abs(c - C) + cost - 30)
    else:
        dfs(a, b, c, cur + 1, cost)
        dfs(a + l[cur], b, c, cur + 1, cost + 10)
        dfs(a, b + l[cur], c, cur + 1, cost + 10)
        dfs(a, b, c + l[cur], cur + 1, cost + 10)


def solve():
    dfs(0, 0, 0, 0, 0)
    print(ans)


if __name__ == '__main__':
    solve()
