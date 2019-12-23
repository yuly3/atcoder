def calc(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return x + 1
    else:
        return 0


def solve():
    A, B = map(int, input().split())
    ans = calc(B)
    if 0 < A:
        ans ^= calc(A-1)
    print(ans)


if __name__ == '__main__':
    solve()
