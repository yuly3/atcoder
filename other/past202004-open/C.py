import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = [list(rl().rstrip()) for _ in range(N)]
    
    for i in range(N - 2, -1, -1):
        for j in range(2 * N - 1):
            if S[i][j] == '#':
                flg = False
                for k in range(-1, 2):
                    if S[i + 1][j + k] == 'X':
                        flg = True
                if flg:
                    S[i][j] = 'X'
    
    for si in S:
        print(*si, sep='')


if __name__ == '__main__':
    solve()
