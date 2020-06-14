import sys

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def make_divisors(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n // i)
    return divisors


def solve():
    _ = int(rl())
    A = list(map(int, rl().split()))
    
    one = A.count(1)
    if one == 1:
        print(1)
        return
    if 2 <= one:
        print(0)
        return
    
    counter = [0] * (10 ** 6 + 1)
    for ai in A:
        for m in range(ai, 10 ** 6 + 1, ai):
            counter[m] += 1
    
    ans = 0
    for ai in A:
        if counter[ai] == 1:
            ans += 1
    print(ans)


if __name__ == '__main__':
    solve()
