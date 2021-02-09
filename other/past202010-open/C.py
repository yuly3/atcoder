import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    s = [rl().rstrip() for _ in range(N)]
    
    ans = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            cnt = 0
            for di in range(-1, 2):
                r = i + di
                for dj in range(-1, 2):
                    c = j + dj
                    if 0 <= r < N and 0 <= c < M:
                        cnt += s[r][c] == '#'
            ans[i][j] = cnt
    print('\n'.join([''.join(map(str, a)) for a in ans]))


if __name__ == '__main__':
    solve()
