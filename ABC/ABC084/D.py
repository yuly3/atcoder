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
    Q = int(input())
    primes = set(eratosthenes(10 ** 5))
    like_2017 = [0] * (10 ** 5 // 2)
    for i in range(3, 10 ** 5, 2):
        if i in primes and (i + 1) // 2 in primes:
            like_2017[i // 2] = like_2017[i // 2 - 1] + 1
        else:
            like_2017[i // 2] = like_2017[i // 2 - 1]
    for _ in range(Q):
        l, r = map(int, input().split())
        ans = like_2017[r // 2] - like_2017[max(0, l // 2 - 1)]
        print(ans)


if __name__ == '__main__':
    solve()
