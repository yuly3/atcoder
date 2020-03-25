import sys
from copy import deepcopy

rl = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


def solve():
    N, Q = map(int, rl().split())
    ans_arr = [[False] * N for _ in range(N)]
    
    for _ in range(Q):
        cmd, *ab = map(int, rl().split())
        if cmd == 1:
            a, b = ab[0] - 1, ab[1] - 1
            ans_arr[a][b] = True
        elif cmd == 2:
            a = ab[0] - 1
            for i in range(N):
                if ans_arr[i][a]:
                    ans_arr[a][i] = True
        else:
            a = ab[0] - 1
            tmp = deepcopy(ans_arr[a])
            for i in range(N):
                if tmp[i]:
                    for j in range(N):
                        if ans_arr[i][j] and a != j:
                            ans_arr[a][j] = True
    
    for i in range(N):
        print(''.join(['Y' if ans_arr[i][j] else 'N' for j in range(N)]))


if __name__ == '__main__':
    solve()
