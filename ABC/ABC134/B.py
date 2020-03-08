def solve():
    N, D = map(int, input().split())

    eye_sight = 1 + D * 2
    ans = N // eye_sight
    if N % eye_sight != 0:
        ans += 1
    print(ans)


if __name__ == '__main__':
    solve()