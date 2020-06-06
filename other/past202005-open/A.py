import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    s = rl().rstrip()
    t = rl().rstrip()
    
    if s == t:
        print('same')
    elif s.lower() == t.lower():
        print('case-insensitive')
    else:
        print('different')


if __name__ == '__main__':
    solve()
