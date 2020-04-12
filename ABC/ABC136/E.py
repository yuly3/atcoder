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
    N, K = map(int, rl().split())
    A = list(map(int, rl().split()))
    
    divs = make_divisors(sum(A))
    divs.sort(reverse=True)
    
    ans = 1
    for div in divs:
        if div == 1:
            break
        a_mods = [ai % div for ai in A]
        a_mods.sort(reverse=True)
        sum_mods = sum(a_mods)
        c = sum_mods // div
        d = sum_mods - sum(a_mods[:c])
        if d <= K:
            ans = div
            break
    print(ans)


if __name__ == '__main__':
    solve()
