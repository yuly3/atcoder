import sys
from math import cos, radians

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, H, M = map(int, rl().split())
    
    rad_h = 0.5 * (60 * H + M)
    rad_m = M * 6
    rad = min(abs(rad_h - rad_m), abs(rad_m - rad_h))
    ans = ((A ** 2) + (B ** 2) - (2 * A * B * cos(radians(rad)))) ** 0.5
    print(ans)


if __name__ == '__main__':
    solve()
