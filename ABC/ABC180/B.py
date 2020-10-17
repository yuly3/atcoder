import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    _ = int(rl())
    x = list(map(int, rl().split()))
    
    print(sum(abs(xi) for xi in x))
    print(sum(xi ** 2 for xi in x) ** 0.5)
    print(abs(max(x, key=abs)))


if __name__ == '__main__':
    solve()
