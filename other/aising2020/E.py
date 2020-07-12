import sys
from heapq import heappush, heappop
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    res = 0
    camel_left, camel_right = [], []
    for _ in range(N):
        K, L, R = map(int, rl().split())
        res += min(L, R)
        if R <= L:
            camel_left.append([K, L, R])
        elif K != N:
            camel_right.append([N - K, L, R])
    
    camel_left.sort(key=itemgetter(0))
    camel_right.sort(key=itemgetter(0))
    
    hq = []
    i = 0
    for j in range(1, N + 1):
        while i < len(camel_left) and camel_left[i][0] == j:
            heappush(hq, camel_left[i][1] - camel_left[i][2])
            i += 1
        while j < len(hq):
            heappop(hq)
    res += sum(hq)
    
    hq = []
    i = 0
    for j in range(1, N):
        while i < len(camel_right) and camel_right[i][0] == j:
            heappush(hq, camel_right[i][2] - camel_right[i][1])
            i += 1
        while j < len(hq):
            heappop(hq)
    res += sum(hq)
    
    return res


if __name__ == '__main__':
    T = int(rl())
    ans = []
    for _ in range(T):
        ans.append(solve())
    print(*ans, sep='\n')
