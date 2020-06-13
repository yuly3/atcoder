import sys
from functools import lru_cache

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, A, B, C, D = map(int, rl().split())
    
    @lru_cache(maxsize=None)
    def calc(t):
        if t == 0:
            return 0
        if t == 1:
            return D
        
        res = min(
            D * t,
            D * abs(t - t // 5 * 5) + C + calc(t // 5),
            D * abs(t - (t + 4) // 5 * 5) + C + calc((t + 4) // 5),
            D * abs(t - t // 3 * 3) + B + calc(t // 3),
            D * abs(t - (t + 2) // 3 * 3) + B + calc((t + 2) // 3),
            D * abs(t - t // 2 * 2) + A + calc(t // 2),
            D * abs(t - (t + 1) // 2 * 2) + A + calc((t + 1) // 2)
        )
        return res
    
    return calc(N)


if __name__ == '__main__':
    T = int(rl())
    ans = []
    for _ in range(T):
        ans.append(solve())
    print(*ans, sep='\n')
