import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    a1, a2, a3 = map(int, rl().split())
    N = a1 + a2 + a3
    
    def check(x, y, z):
        if x != tuple(sorted(x)) or y != tuple(sorted(y)) or z != tuple(sorted(z)):
            return False
        for i, j in zip(x, y):
            if j <= i:
                return False
        for i, j in zip(y, z):
            if j <= i:
                return False
        return True
    
    ans = 0
    for p in permutations(range(1, N + 1), r=N):
        t1 = p[:a1]
        t2 = p[a1:a1 + a2]
        t3 = p[a1 + a2:]
        ans += check(t1, t2, t3)
    print(ans)


if __name__ == '__main__':
    solve()
