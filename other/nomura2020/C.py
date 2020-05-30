import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    if N != 0 and A[0] != 0:
        print(-1)
        return
    if N == 0 and A[0] != 1:
        print(-1)
        return
    
    v = [1]
    m = 2
    for ai in A[1:]:
        v.append(m)
        if m < ai:
            print(-1)
            return
        m -= ai
        m *= 2
    
    m = min(v[-1], A[-1])
    ans = m
    for i in range(N - 1, -1, -1):
        m = min(m + A[i], v[i])
        ans += m
    print(ans)


if __name__ == '__main__':
    solve()
