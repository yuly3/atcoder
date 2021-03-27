import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline

ans = 2 ** 30


def solve():
    N = int(rl())
    A = list(map(int, rl().split()))
    
    def f(sl, cur):
        if cur == N - 1:
            sl |= 1 << (N - 1)
            prev = 0
            x = 0
            for i in range(N):
                if sl >> i & 1:
                    o = 0
                    for ai in A[prev:i + 1]:
                        o |= ai
                    x ^= o
                    prev = i + 1
            global ans
            ans = min(ans, x)
        else:
            f(sl | (1 << cur), cur + 1)
            f(sl, cur + 1)
    
    f(0, 0)
    global ans
    print(ans)


if __name__ == '__main__':
    solve()
