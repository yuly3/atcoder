import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    
    if 'atcoder' < S:
        return 0
    if all(si == 'a' for si in S):
        return -1
    
    for i, si in enumerate(S):
        if si != 'a':
            if si <= 't':
                return i
            else:
                return i - 1


if __name__ == '__main__':
    ans = []
    T = int(rl())
    for _ in range(T):
        ans.append(str(solve()))
    print('\n'.join(ans))
