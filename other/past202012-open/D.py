import sys
from operator import itemgetter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = [rl().rstrip() for _ in range(N)]
    
    m = []
    for i, si in enumerate(S):
        cnt = 0
        for sij in si:
            if sij != '0':
                break
            cnt += 1
        m.append((int(si), -cnt, si))
    m.sort(key=itemgetter(0, 1))
    
    ans = []
    for _, _, si in m:
        ans.append(si)
    print(*ans, sep='\n')


if __name__ == '__main__':
    solve()
