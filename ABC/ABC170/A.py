import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    x = list(map(int, rl().split()))
    
    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            return


if __name__ == '__main__':
    solve()
