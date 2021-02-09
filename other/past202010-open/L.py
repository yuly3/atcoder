import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q = map(int, rl().split())
    h = list(map(int, rl().split()))
    
    d = [0] * (N - 1)
    odd_sub_even = defaultdict(int)
    even_sub_odd = defaultdict(int)
    for i in range(N - 1):
        di = h[i] - h[i + 1]
        d[i] = di
        if i % 2 == 0:
            odd_sub_even[di] += 1
        else:
            even_sub_odd[di] += 1
    
    ans = []
    odd, even = 0, 0
    for _ in range(Q):
        cmd, *uv = map(int, rl().split())
        if cmd == 1:
            v = uv[0]
            odd += v
        elif cmd == 2:
            v = uv[0]
            even += v
        else:
            u, v = uv
            u -= 1
            if u < N - 1:
                if u % 2 == 0:
                    odd_sub_even[d[u]] -= 1
                    odd_sub_even[d[u] + v] += 1
                else:
                    even_sub_odd[d[u]] -= 1
                    even_sub_odd[d[u] + v] += 1
                d[u] += v
            if 0 < u:
                if u % 2 == 0:
                    even_sub_odd[d[u - 1]] -= 1
                    even_sub_odd[d[u - 1] - v] += 1
                else:
                    odd_sub_even[d[u - 1]] -= 1
                    odd_sub_even[d[u - 1] - v] += 1
                d[u - 1] -= v
        ans.append(odd_sub_even[-(odd - even)] + even_sub_odd[-(even - odd)])
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
