import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    def check(t):
        cnt = 0
        for ai in A:
            cnt += -(-ai // t) - 1
        return cnt <= K
    
    ok, ng = 10 ** 9, 0
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if check(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
