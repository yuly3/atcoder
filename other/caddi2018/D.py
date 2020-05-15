import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    a = [int(rl()) for _ in range(N)]
    
    print('second' if all(ai % 2 == 0 for ai in a) else 'first')


if __name__ == '__main__':
    solve()
