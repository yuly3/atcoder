import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, C = map(int, rl().split())

    dp = [[[0.] * 101 for _ in range(101)] for _ in range(101)]

    def f(x, y, z):
        if 100 in (x, y, z):
            return 0
        if dp[x][y][z] != 0.:
            return dp[x][y][z]

        inc_x = f(x + 1, y, z) + 1
        inc_y = f(x, y + 1, z) + 1
        inc_z = f(x, y, z + 1) + 1
        den = x + y + z
        res = (x * inc_x + y * inc_y + z * inc_z) / den
        dp[x][y][z] = res
        return res

    print(f(A, B, C))


if __name__ == '__main__':
    solve()
