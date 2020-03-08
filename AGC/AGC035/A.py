def solve():
    N = int(input())
    numbers = list(map(int, input().split()))

    x = 0
    for num in numbers:
        x ^= num

    if x == 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
