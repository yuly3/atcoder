def solve():
    N = int(input())
    A = list(map(int, input().split()))
    
    ans = 10 ** 9
    for i in range(N):
        cnt = 0
        ai = A[i]
        while 1:
            if ai % 2 == 0:
                ai //= 2
                cnt += 1
            else:
                break
        ans = min(ans, cnt)
    print(ans)


if __name__ == '__main__':
    solve()
