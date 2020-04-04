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
    N = int(rl())
    
    divisors1 = set(make_divisors(N - 1)[1:])
    divisors2 = set(make_divisors(N)[1:])
    
    for divisor in divisors2:
        tmp = N
        while tmp % divisor == 0:
            tmp //= divisor
        if tmp % divisor == 1:
            divisors1.add(divisor)
    print(len(divisors1))


if __name__ == '__main__':
    solve()
