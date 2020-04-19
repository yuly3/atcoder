import math
import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    R = int(rl())
    ans = 2 * R * math.pi
    print(ans)


if __name__ == '__main__':
    solve()
