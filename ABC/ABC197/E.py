import sys
from collections import defaultdict
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    XC = [list(map(int, rl().split())) for _ in range(N)]
    
    dic = defaultdict(list)
    for xi, ci in XC:
        dic[ci].append(xi)
    
    ar = []
    for key, ls in dic.items():
        ar.append((key, min(ls), max(ls)))
    ar.sort(key=itemgetter(0))
    
    ans1 = abs(ar[0][2]) + ar[0][2] - ar[0][1]
    cur1 = ar[0][1]
    ans2 = abs(ar[0][1]) + ar[0][2] - ar[0][1]
    cur2 = ar[0][2]
    for i in range(1, len(ar)):
        _, mi, ma = ar[i]
        x, y = ans1, ans2
        c1, c2 = cur1, cur2
        d1 = abs(c1 - mi)
        d2 = abs(c2 - mi)
        if x + d1 < y + d2:
            ans2 = x + d1 + ma - mi
        else:
            ans2 = y + d2 + ma - mi
        cur2 = ma
        d1 = abs(c1 - ma)
        d2 = abs(c2 - ma)
        if x + d1 < y + d2:
            ans1 = x + d1 + ma - mi
        else:
            ans1 = y + d2 + ma - mi
        cur1 = mi
    ans1 += abs(ar[-1][1])
    ans2 += abs(ar[-1][2])
    print(min(ans1, ans2))


if __name__ == '__main__':
    solve()
