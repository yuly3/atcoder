import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def small_solve(a, k, b):
    p = a
    for _ in range(k):
        p = b[p - 1]
    print(p)


def big_solve(a, k, b):
    p_set = set()
    p = a
    while p not in p_set:
        p_set.add(p)
        p = b[p - 1]
    
    roop_s = p
    cnt0 = len(p_set)
    
    p_set = set()
    while p not in p_set:
        p_set.add(p)
        p = b[p - 1]
    
    cnt1 = len(p_set)
    mod = 0
    for ki in k:
        mod = (mod * 10 + int(ki)) % cnt1
    mod = (mod - cnt0) % cnt1
    
    small_solve(roop_s, mod, b)


def solve():
    N, a = map(int, rl().split())
    k = rl().rstrip()
    b = list(map(int, rl().split()))
    
    if int(k) <= N:
        small_solve(a, int(k), b)
    else:
        big_solve(a, k, b)


if __name__ == '__main__':
    solve()
