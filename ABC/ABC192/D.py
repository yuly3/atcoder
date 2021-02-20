import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    X = rl().rstrip()
    M = int(rl())
    
    d = max(int(xi) for xi in X)
    
    def check(t):
        su = 0
        for i, xi in enumerate(X):
            su *= t
            su += int(xi)
            if M < su:
                break
        return su <= M
    
    if len(X) == 1:
        if int(X) > M:
            print(0)
        else:
            print(1)
        return
    
    ok, ng = d, M + 1
    while 1 < ng - ok:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok - d)


if __name__ == '__main__':
    solve()
