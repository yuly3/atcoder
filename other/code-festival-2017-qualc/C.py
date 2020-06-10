import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    s = rl().rstrip()
    
    que = deque(s)
    ans = 0
    while 1 < len(que):
        if que[0] == que[-1]:
            que.pop()
            que.popleft()
        elif que[0] == 'x':
            que.append('x')
            ans += 1
        elif que[-1] == 'x':
            que.appendleft('x')
            ans += 1
        else:
            print(-1)
            return
    print(ans)


if __name__ == '__main__':
    solve()
