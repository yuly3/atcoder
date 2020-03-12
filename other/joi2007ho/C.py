from bisect import bisect_right
from itertools import combinations_with_replacement


def solve():
    N, M, *P = map(int, open(0).read().split())
    
    P += [0]
    point_half = []
    for p1, p2 in combinations_with_replacement(P, 2):
        if p1 + p2 <= M:
            point_half.append(p1 + p2)
    point_half.sort()
    
    ans = 0
    for p in point_half:
        index = bisect_right(point_half, M - p) - 1
        ans = max(ans, p + point_half[index])
    print(ans)


if __name__ == '__main__':
    solve()
