import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q = map(int, rl().split())
    
    under = [-1] * N
    top = list(range(N))
    
    for _ in range(Q):
        f, t, x = map(lambda v: int(v) - 1, rl().split())
        top_f = top[f]
        top_t = top[t]
        top[f] = under[x]
        top[t] = top_f
        under[x] = top_t
    
    ans = [0] * N
    for idx, con in enumerate(top):
        if con == -1:
            continue
        c = con
        while c != -1:
            ans[c] = idx + 1
            c = under[c]
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
