import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    K = int(rl())
    S = rl().rstrip()
    
    if len(S) <= K:
        print(S)
    else:
        print(S[:K] + '...')


if __name__ == '__main__':
    solve()
