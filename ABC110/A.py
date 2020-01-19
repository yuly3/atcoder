from itertools import permutations


def solve():
    A, B, C = map(str, input().split())
    ans = 0
    for a, b, c in permutations(A + B + C, 3):
        ans = max(ans, int(a + b) + int(c))
    print(ans)


if __name__ == '__main__':
    solve()
