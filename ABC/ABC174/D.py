import sys
from collections import Counter

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    c = rl().rstrip()
    
    counter = Counter(c)
    red = counter['R']
    white = counter['W']
    
    red -= c[:red].count('R')
    white -= c[-white:].count('W')
    print(min(red, white))


if __name__ == '__main__':
    solve()
