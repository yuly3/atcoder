import sys
from collections import defaultdict

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = [rl().rstrip() for _ in range(N)]
    
    counter = defaultdict(int)
    for si in S:
        counter[si] += 1
    
    print('AC x ' + str(counter['AC']))
    print('WA x ' + str(counter['WA']))
    print('TLE x ' + str(counter['TLE']))
    print('RE x ' + str(counter['RE']))


if __name__ == '__main__':
    solve()
