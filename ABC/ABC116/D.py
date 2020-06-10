import sys
from collections import defaultdict
from heapq import heappush, heappop
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    td = [list(map(int, rl().split())) for _ in range(N)]
    
    td.sort(key=itemgetter(1), reverse=True)
    hq = []
    counter = defaultdict(int)
    t_set = set()
    d_sum = 0
    for i in range(K):
        ti, di = td[i]
        t_set.add(ti)
        counter[ti] += 1
        if 1 < counter[ti]:
            heappush(hq, di)
        d_sum += di
    
    ans = d_sum + len(t_set) * len(t_set)
    for i in range(K, N):
        ti, di = td[i]
        if ti in t_set:
            continue
        if not hq:
            break
        dj = heappop(hq)
        d_sum -= dj
        d_sum += di
        t_set.add(ti)
        ans = max(ans, d_sum + len(t_set) * len(t_set))
    print(ans)


if __name__ == '__main__':
    solve()
