import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S = rl().rstrip()
    if 'RRR' == S:
        print(3)
    elif 'RR' in S:
        print(2)
    elif 'R' in S:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    solve()
