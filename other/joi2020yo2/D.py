import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    cost = (
        (0, 1, 2, 3, 2, 3, 4, 3, 4, 5),
        (1, 0, 1, 2, 1, 2, 3, 2, 3, 4),
        (2, 1, 0, 1, 2, 1, 2, 3, 2, 3),
        (3, 2, 1, 0, 3, 2, 1, 4, 3, 2),
        (2, 1, 2, 3, 0, 1, 2, 1, 2, 3),
        (3, 2, 1, 2, 1, 0, 1, 2, 1, 2),
        (4, 3, 2, 1, 2, 1, 0, 3, 2, 1),
        (3, 2, 3, 4, 1, 2, 3, 0, 1, 2),
        (4, 3, 2, 3, 2, 1, 2, 1, 0, 1),
        (5, 4, 3, 2, 3, 2, 1, 2, 1, 0)
    )
    
    M, R = map(int, rl().split())
    INF = 10 ** 7
    dist = [[INF] * 10 for _ in range(M)]
    dist[0][0] = 0
    que = deque([(0, 0)])
    while que:
        cur, mod = que.popleft()
        for nx in range(10):
            nmod = (10 * mod + nx) % M
            nd = dist[mod][cur] + cost[cur][nx] + 1
            if nd < dist[nmod][nx]:
                dist[nmod][nx] = nd
                que.append((nx, nmod))
    print(min(dist[R]))


if __name__ == '__main__':
    solve()
