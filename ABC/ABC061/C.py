import sys
from operator import itemgetter

rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    ab = [list(map(int, rl().split())) for _ in range(N)]
    ab.sort(key=itemgetter(0))
    
    cnt = 0
    for a, b in ab:
        cnt += b
        if K <= cnt:
            print(a)
            exit()


if __name__ == '__main__':
    solve()
