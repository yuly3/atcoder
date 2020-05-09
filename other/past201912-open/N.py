import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, W, C = map(int, rl().split())
    compress = defaultdict(int)
    for _ in range(N):
        left, right, p = map(int, rl().split())
        compress[right] -= p
        compress[max(0, left - C + 1)] += p
    
    compress_keys = tuple(sorted(compress.keys()))
    if C <= compress_keys[0]:
        print(0)
        return
    
    ans = 10 ** 18
    tmp = 0
    for key in compress_keys:
        if W - C < key:
            break
        tmp += compress[key]
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    solve()
