import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X, K, D = map(int, rl().split())
    X = abs(X)
    
    if K < X // D:
        print(X - D * K)
        return
    
    ans = X - D * (X // D)
    K -= X // D
    if K % 2 == 0:
        print(ans)
    else:
        print(abs(ans - D))


if __name__ == '__main__':
    solve()
