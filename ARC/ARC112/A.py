import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    L, R = map(int, rl().split())
    
    max_c = R - L
    if max_c < L:
        return 0
    x = R - 2 * L + 1
    y = R - max_c - L + 1
    ret = (x + y) * (x - y + 1) // 2
    return ret


if __name__ == '__main__':
    T = int(rl())
    ans = []
    for _ in range(T):
        ans.append(solve())
    print('\n'.join(map(str, ans)))
