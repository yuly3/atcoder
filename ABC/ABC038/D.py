from bisect import bisect_left


def solve():
    N = int(input())
    wh = [[] for _ in range(N)]
    for i in range(N):
        wh[i] = list(map(int, input().split()))
    
    wh.sort(key=lambda x: (x[0], -x[1]))
    
    INF = 10**7
    ok = [INF]*(N+1)
    for _, h in wh:
        index = bisect_left(ok, h)
        ok[index] = h
    print(ok.index(INF))


if __name__ == '__main__':
    solve()
