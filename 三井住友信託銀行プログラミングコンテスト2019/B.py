def solve():
    N = int(input())
    ans = N / 108 * 100

    if int(int(ans)*1.08) == N:
        print(int(ans))
    elif int(int(ans+1)*1.08) == N:
        print(int(ans+1))
    else:
        print(':(')


if __name__ == '__main__':
    solve()