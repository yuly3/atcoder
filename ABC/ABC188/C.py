import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    player = deque([(i, ai) for i, ai in enumerate(A)])
    for i in range(1, N):
        for _ in range(2 ** (N - i)):
            p0, r0 = player.popleft()
            p1, r1 = player.popleft()
            if r0 < r1:
                player.append((p1, r1))
            else:
                player.append((p0, r0))
    
    a, b = player.popleft()
    c, d = player.popleft()
    if b < d:
        print(a + 1)
    else:
        print(c + 1)


if __name__ == '__main__':
    solve()
