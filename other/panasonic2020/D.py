import sys
rline = sys.stdin.readline

N = int(input())


def dfs(ans, max_c):
    if len(ans) == N:
        print(ans)
    else:
        for i in range(max_c + 1):
            dfs(ans + chr(ord('a') + i), max_c + 1 if i == max_c else max_c)


def solve():
    dfs('', 0)


if __name__ == '__main__':
    solve()
