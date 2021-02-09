import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, Y = map(float, rl().split())
    if Y == 0:
        print('ERROR')
        return
    
    n = str(X / Y)
    n = n[:n.index('.') + 3]
    print('{:.2f}'.format(float(n)))


if __name__ == '__main__':
    solve()
