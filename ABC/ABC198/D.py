import sys
from itertools import permutations

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    S1 = rl().rstrip()
    S2 = rl().rstrip()
    S3 = rl().rstrip()
    
    ss = set(S1) | set(S2)
    for nums in permutations(range(10), len(ss)):
        di = dict()
        for num, s in zip(nums, ss):
            di[s] = num
        if di[S1[0]] == 0 or di[S2[0]] == 0:
            continue
        n = m = 0
        for i, si in enumerate(S1[::-1]):
            n += di[si] * 10 ** i
        for i, si in enumerate(S2[::-1]):
            m += di[si] * 10 ** i
        num3 = n + m
        if len(str(num3)) != len(S3):
            continue
        flg = True
        for i, num3i in enumerate(str(num3)):
            if S3[i] in di and di[S3[i]] != int(num3i):
                flg = False
                break
            if S3[i] not in di and int(num3i) in di.values():
                flg = False
                break
            if S3[i] not in di:
                di[S3[i]] = int(num3i)
        if flg:
            print(n)
            print(m)
            print(num3)
            exit()
    print('UNSOLVABLE')


if __name__ == '__main__':
    solve()
