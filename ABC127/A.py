def solve():
    A, B = map(int, input().split())
    if 13 <= A:
        print(B)
    elif 6 <= A <= 12:
        print(B//2)
    else:
        print(0)


if __name__ == '__main__':
    solve()