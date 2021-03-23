import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y = map(int, rl().split())
    
    @lru_cache(maxsize=None)
    def f(y):
        if y == 1:
            return abs(X - y)
        if y % 2 == 1:
            return min(abs(X - y), f((y + 1) // 2) + 2, f((y - 1) // 2) + 2)
        return min(abs(X - y), f(y // 2) + 1)
    
    ans = f(Y)
    print(ans)


if __name__ == '__main__':
    solve()
