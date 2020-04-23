import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    sx, sy, tx, ty = map(int, rl().split())
    dx, dy = tx - sx, ty - sy
    
    ans = 'U' * dy + 'R' * dx
    ans += 'D' * dy + 'L' * dx
    ans += 'L' + 'U' * (dy + 1) + 'R' * (dx + 1) + 'D'
    ans += 'R' + 'D' * (dy + 1) + 'L' * (dx + 1) + 'U'
    print(ans)


if __name__ == '__main__':
    solve()
