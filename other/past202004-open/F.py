import sys
from collections import deque
from operator import itemgetter
from heapq import heappop, heappush

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    AB = [list(map(int, rl().split())) for _ in range(N)]
    AB.sort(key=itemgetter(0))
    AB = deque(AB)
    
    ans = [0] * (N + 1)
    task_hq = []
    for i in range(1, N + 1):
        while AB and AB[0][0] == i:
            _, b = AB.popleft()
            heappush(task_hq, -b)
        ans[i] = ans[i - 1] - heappop(task_hq)
    print(*ans[1:], sep='\n')


if __name__ == '__main__':
    solve()
