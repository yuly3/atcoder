import sys
import heapq as hq
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N, Q = map(int, rl().split())
    event = []
    for _ in range(N):
        s, t, x = map(int, rl().split())
        event.append((t - x, 0, x))
        event.append((s - x, 1, x))
    for _ in range(Q):
        d = int(rl())
        event.append((d, 2, -1))
    event.sort(key=itemgetter(0, 1))
    
    pos_set = set()
    pos_hq = []
    ans = []
    for _, com, pos in event:
        if com == 0:
            pos_set.remove(pos)
        elif com == 1:
            pos_set.add(pos)
            hq.heappush(pos_hq, pos)
        else:
            while pos_hq:
                if pos_hq[0] not in pos_set:
                    hq.heappop(pos_hq)
                else:
                    break
            ans.append(pos_hq[0] if pos_hq else -1)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
