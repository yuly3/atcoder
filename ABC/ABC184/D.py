import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, C = map(int, rl().split())
    
    @lru_cache(maxsize=None)
    def f(x, y, z):
        if x == 100 or y == 100 or z == 100:
            return 0
        
        den = x + y + z
        return x / den * (f(x + 1, y, z) + 1) + y / den * (f(x, y + 1, z) + 1) + z / den * (f(x, y, z + 1) + 1)
    
    print(f(A, B, C))


if __name__ == '__main__':
    solve()
