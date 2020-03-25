import sys
rl = sys.stdin.readline


def solve():
    N, A, B = map(int, rl().split())
    h = [int(rl()) for _ in range(N)]
    ad_d = A - B
    
    def calc(t):
        cnt = 0
        for i in range(N):
            d = h[i] - B * t
            if 0 < d:
                cnt += d // ad_d if d % ad_d == 0 else d // ad_d + 1
        return cnt <= t
    
    ok, ng = 10 ** 9, 0
    while 1 < ok - ng:
        mid = (ok + ng) // 2
        if calc(mid):
            ok = mid
        else:
            ng = mid
    print(ok)


if __name__ == '__main__':
    solve()
