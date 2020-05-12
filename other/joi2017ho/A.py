import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q, S, T = map(int, rl().split())
    A = [int(rl()) for _ in range(N + 1)]
    LRX = [list(map(int, rl().split())) for _ in range(Q)]
    
    tmp = 0
    a_sub = [0] * (N + 1)
    for i in range(N):
        sub = A[i + 1] - A[i]
        a_sub[i + 1] = sub
        tmp -= sub * S if 0 <= sub else sub * T
    
    ans = []
    for li, ri, xi in LRX:
        tmp += a_sub[li] * S if 0 <= a_sub[li] else a_sub[li] * T
        a_sub[li] += xi
        tmp -= a_sub[li] * S if 0 <= a_sub[li] else a_sub[li] * T
        
        if ri < N:
            ri += 1
            tmp += a_sub[ri] * S if 0 <= a_sub[ri] else a_sub[ri] * T
            a_sub[ri] -= xi
            tmp -= a_sub[ri] * S if 0 <= a_sub[ri] else a_sub[ri] * T
        
        ans.append(tmp)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
