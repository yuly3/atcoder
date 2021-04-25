import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    Q = int(rl())
    
    first = list(S[:N])
    latter = list(S[N:])
    flip = 0
    for _ in range(Q):
        ti, ai, bi = map(int, rl().split())
        ai, bi = ai - 1, bi - 1
        if ti == 1:
            if flip:
                if N <= ai and N <= bi:
                    first[ai - N], first[bi - N] = first[bi - N], first[ai - N]
                elif ai >= N > bi:
                    first[ai - N], latter[bi] = latter[bi], first[ai - N]
                elif ai < N <= bi:
                    latter[ai], first[bi - N] = first[bi - N], latter[ai]
                else:
                    latter[bi], latter[ai] = latter[ai], latter[bi]
            else:
                if N <= ai and N <= bi:
                    latter[ai - N], latter[bi - N] = latter[bi - N], latter[ai - N]
                elif ai >= N > bi:
                    latter[ai - N], first[bi] = first[bi], latter[ai - N]
                elif ai < N <= bi:
                    first[ai], latter[bi - N] = latter[bi - N], first[ai]
                else:
                    first[ai], first[bi] = first[bi], first[ai]
        else:
            flip ^= 1
    if flip:
        first, latter = latter, first
    print(''.join(first) + ''.join(latter))


if __name__ == '__main__':
    solve()
