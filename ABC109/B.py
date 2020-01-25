from collections import defaultdict


def solve():
    N = int(input())
    w_dict = defaultdict(int)
    pw = input()
    w_dict[pw] = 1
    for _ in range(N - 1):
        cw = input()
        if cw[0] != pw[-1] or w_dict[cw] == 1:
            print('No')
            exit()
        w_dict[cw] = 1
        pw = cw
    print('Yes')


if __name__ == '__main__':
    solve()
