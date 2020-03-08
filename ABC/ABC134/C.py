def solve():
    N = int(input())
    biggest = 0
    second_biggest = 0
    a_l = [0] * N

    for i in range(N):
        a_l[i] = int(input())
        if biggest <= a_l[i]:
            second_biggest = biggest
            biggest = a_l[i]
        elif second_biggest <= a_l[i]:
            second_biggest = a_l[i]

    for i in range(N):
        if a_l[i] == biggest:
            print(second_biggest)
        else:
            print(biggest)


if __name__ == '__main__':
    solve()