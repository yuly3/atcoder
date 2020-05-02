import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K = int(rl())
    A, B = map(int, rl().split())
    
    for i in range(A, B + 1):
        if i % K == 0:
            print('OK')
            exit()
    print('NG')


if __name__ == '__main__':
    solve()
