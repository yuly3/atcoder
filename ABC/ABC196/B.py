import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = rl().rstrip()
    
    idx = X.find('.')
    if idx == -1:
        print(X)
    else:
        print(X[:idx])


if __name__ == '__main__':
    solve()
