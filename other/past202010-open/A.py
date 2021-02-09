import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    ABC = list(map(int, rl().split()))
    ABC = [(v, i) for i, v in enumerate(ABC)]
    ABC.sort()
    print(chr(ord('A') + ABC[1][1]))


if __name__ == '__main__':
    solve()
