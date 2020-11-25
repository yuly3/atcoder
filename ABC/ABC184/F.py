import sys
from bisect import bisect_right

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, T = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    def f(problems):
        stack = [(0, 0)]
        res = []
        while stack:
            cost, nex = stack.pop()
            if nex == len(problems):
                res.append(cost)
                continue
            stack.append((cost, nex + 1))
            stack.append((cost + problems[nex], nex + 1))
        return res
    
    t0 = f(A[:N // 2])
    t1 = f(A[N // 2:])
    t1.sort()
    
    ans = 0
    for x in t0:
        if T < x:
            continue
        idx = bisect_right(t1, T - x) - 1
        ans = max(ans, x + t1[idx])
    print(ans)


if __name__ == '__main__':
    solve()
