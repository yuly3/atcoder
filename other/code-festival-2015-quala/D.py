import sys

rl = sys.stdin.readline


def solve():
    N, M = map(int, rl().split())
    X = [int(rl()) for _ in range(M)]
    
    def calc(t):
        a = 1
        for xi in X:
            if t < xi - a:
                return False
            a = min(a, xi)
            a = xi + max(t - 2 * (xi - a), (t - (xi - a)) // 2) + 1
        return N < a
    
    ok, ng = 10 ** 12, -1
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if calc(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
