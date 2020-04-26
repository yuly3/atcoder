import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, C, D = map(int, rl().split())
    for i in range(200):
        if i % 2 == 0:
            C -= B
            if C <= 0:
                print('Yes')
                exit()
        else:
            A -= D
            if A <= 0:
                print('No')
                exit()


if __name__ == '__main__':
    solve()
