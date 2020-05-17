import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = rl().rstrip()
    
    s = N[-1]
    if s == '2' or s == '4' or s == '5' or s == '7' or s == '9':
        print('hon')
    elif s == '0' or s == '1' or s == '6' or s == '8':
        print('pon')
    else:
        print('bon')


if __name__ == '__main__':
    solve()
