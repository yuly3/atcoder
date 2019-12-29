import math
from bisect import bisect_left


def eratosthenes(n):
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def solve():
    X = int(input())
    primes = eratosthenes(100010)
    index = bisect_left(primes, X)
    print(primes[index])


if __name__ == '__main__':
    solve()
