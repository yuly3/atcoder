import sys
from math import ceil

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    ans = [0] * (N + 1)
    for x in range(1, ceil(N ** 0.5) + 1):
        for y in range(1, ceil(N ** 0.5) + 1):
            for z in range(1, ceil(N ** 0.5) + 1):
                n = x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x
                if n <= N:
                    ans[n] += 1
    print(*ans[1:], sep='\n')


if __name__ == '__main__':
    solve()
