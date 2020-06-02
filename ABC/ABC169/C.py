import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = rl().split()
    A = int(A)
    B = B.split('.')
    B = int(B[0] + B[1])
    ans = A * B // 100
    print(ans)


if __name__ == '__main__':
    solve()
