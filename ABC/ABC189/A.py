import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    C = rl().rstrip()
    if len(set(C)) == 1:
        print('Won')
    else:
        print('Lost')


if __name__ == '__main__':
    solve()
