import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline

ans = 0
N, M, Q = map(int, rl().split())
abcd = [list(map(int, rl().split())) for _ in range(Q)]


def calc(A):
    if len(A) == N:
        tmp = 0
        for a, b, c, d in abcd:
            if A[b - 1] - A[a - 1] == c:
                tmp += d
        global ans
        ans = max(ans, tmp)
    else:
        for i in range(A[-1], M + 1):
            calc(A + [i])


def solve():
    for i in range(1, M + 1):
        calc([i])
    print(ans)


if __name__ == '__main__':
    solve()
