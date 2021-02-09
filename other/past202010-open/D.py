import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    N = int(rl())
    S = rl().rstrip()
    
    pos = []
    for i in range(N):
        if S[i] == '#':
            pos.append(i)
    
    min_sum = 200
    ans_x, ans_y = 0, 0
    for x in range(N):
        ns = list(S)
        for y in range(N):
            for p in pos:
                for d in range(-x, y + 1):
                    c = p + d
                    if 0 <= c < N:
                        ns[c] = '#'
            if '.' not in ns and x + y < min_sum:
                min_sum = x + y
                ans_x, ans_y = x, y
    print(ans_x, ans_y)


if __name__ == '__main__':
    solve()
