from bisect import bisect_left, bisect_right


def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    
    A.sort()
    C.sort()
    
    ans = 0
    for i in range(N):
        cnt_a = bisect_left(A, B[i])
        cnt_b = N - bisect_right(C, B[i])
        ans += cnt_a * cnt_b
    print(ans)


if __name__ == '__main__':
    solve()
