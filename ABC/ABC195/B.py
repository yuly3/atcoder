import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B, W = map(int, rl().split())
    W *= 1000
    
    ma = W // A
    mi = -(-W // B)
    print('UNSATISFIABLE' if ma < mi else f'{mi} {ma}')


if __name__ == '__main__':
    solve()
