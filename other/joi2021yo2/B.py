import sys
from collections import deque, Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q = map(int, rl().split())
    ord_A = ord('A')
    
    dist = [-1] * 3 ** N
    ans = []
    for _ in range(Q):
        s = rl().rstrip()
        t = ''
        for si in s:
            t += str(ord(si) - ord_A)
        int_t = int(t[::-1], 3)
        if dist[int_t] != -1:
            ans.append(dist[int_t])
            continue
        counter = Counter(t)
        ss = '0' * counter['0'] + '1' * counter['1'] + '2' * counter['2']
        st = int(ss[::-1], 3)
        dist[st] = 0
        que = deque([st])
        while que:
            c = que.popleft()
            x, y = 0, 1
            for i in range(N):
                x = x * 3 + c // y % 3
                y *= 3
                nc = c // y * y + x
                if dist[nc] == -1:
                    dist[nc] = dist[c] + 1
                    que.append(nc)
        ans.append(dist[int_t])
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    solve()
