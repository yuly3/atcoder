def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    return divisors


def solve():
    N, M = map(int, input().split())
    
    divs = make_divisors(M)
    ans = 0
    for div in divs:
        if div <= M / N:
            ans = max(ans, div)
    print(ans)


if __name__ == '__main__':
    solve()
