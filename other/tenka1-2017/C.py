import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    
    for h in range(1, 3501):
        for n in range(1, 3501):
            denom = 4 * h * n - N * n - N * h
            if denom == 0:
                continue
            w = (N * h * n) / denom
            if w.is_integer() and 0 < w:
                print(h, n, int(w))
                return


if __name__ == '__main__':
    solve()
