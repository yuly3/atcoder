from itertools import permutations


def solve():
    N = int(input())
    P = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    
    a, b = -1, -1
    cnt = 0
    for nums in permutations(range(1, N + 1), N):
        nums = list(nums)
        if nums == P:
            a = cnt
        if nums == Q:
            b = cnt
        cnt += 1
    print(abs(a - b))


if __name__ == '__main__':
    solve()
