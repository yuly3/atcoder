def eratosthenes(n):
    prime = [2]
    if n == 2:
        return prime
    limit = int(n ** 0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]


def solve():
    N = int(input())
    primes = eratosthenes(55555)
    ans = []
    for p in primes:
        if p % 5 == 1:
            ans.append(p)
    print(' '.join(map(str, ans[:N])))


if __name__ == '__main__':
    solve()
