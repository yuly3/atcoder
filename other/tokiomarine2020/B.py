import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, V = map(int, rl().split())
    B, W = map(int, rl().split())
    T = int(rl())
    
    if V <= W:
        print('NO')
        return
    d = abs(A - B)
    if d / (V - W) <= T:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    solve()
