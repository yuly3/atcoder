import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y = map(int, rl().split())
    
    for i in range(X + 1):
        if 2 * i + 4 * (X - i) == Y:
            print('Yes')
            return
    print('No')


if __name__ == '__main__':
    solve()
