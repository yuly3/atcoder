import sys
from copy import deepcopy

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    H, W, K = map(int, rl().split())
    c = [list(rl().rstrip()) for _ in range(H)]
    
    ans = 0
    for sh in range(1 << H):
        for sw in range(1 << W):
            cc = deepcopy(c)
            for y in range(H):
                if sh >> y & 1:
                    for x in range(W):
                        cc[y][x] = '.'
            for x in range(W):
                if sw >> x & 1:
                    for y in range(H):
                        cc[y][x] = '.'
            cnt = 0
            for y in range(H):
                for x in range(W):
                    cnt += cc[y][x] == '#'
            ans += cnt == K
    print(ans)


if __name__ == '__main__':
    solve()
