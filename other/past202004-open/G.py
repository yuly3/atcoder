import sys
from collections import deque, defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    Q = int(rl())
    
    ans = []
    S = deque([])
    for _ in range(Q):
        query = list(rl().split())
        if query[0] == '1':
            c, x = query[1], int(query[2])
            S.append([x, c])
        else:
            d = int(query[1])
            del_items = defaultdict(int)
            while S and S[0][0] <= d and d:
                x, c = S.popleft()
                del_items[c] += x
                d -= x
            if S and d:
                c = S[0][1]
                del_items[c] += d
                S[0][0] -= d
            tmp = 0
            for val in del_items.values():
                tmp += val ** 2
            ans.append(tmp)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
