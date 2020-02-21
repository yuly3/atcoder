def solve():
    N = int(input())
    A, B = [0] * N, [0] * N
    for i in range(N):
        A[i], B[i] = map(int, input().split())
    
    ans = 10 ** 9 * 30
    for s in A + B:
        for t in A + B:
            time = 0
            for i in range(N):
                time += abs(s - A[i]) + abs(A[i] - B[i]) + abs(B[i] - t)
            ans = min(ans, time)
    print(ans)


if __name__ == '__main__':
    solve()
