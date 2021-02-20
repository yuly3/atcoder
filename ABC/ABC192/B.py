import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    
    for i, si in enumerate(S):
        if i % 2 == 0 and si.isupper() or i % 2 == 1 and si.islower():
            print('No')
            return
    print('Yes')


if __name__ == '__main__':
    solve()
