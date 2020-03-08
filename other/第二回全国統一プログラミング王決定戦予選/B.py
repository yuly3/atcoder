import sys
import collections


def solve():
    MOD = 998244353
    N, *d_l = map(int, open(0).read().split())
    ans = 1

    if d_l[0] != 0:
        print(0)
        sys.exit()

    d_max = max(d_l)
    count_dic = collections.Counter(d_l)
    if count_dic[0] != 1:
        print(0)
        sys.exit()

    for i in range(2, d_max + 1):
        ans *= count_dic[i - 1] ** count_dic[i]

    print(ans % MOD)


if __name__ == '__main__':
    solve()