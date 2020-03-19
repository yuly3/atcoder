def solve():
    N = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    
    sum_cost = 0
    for i in range(1, N + 2):
        sum_cost += abs(A[i - 1] - A[i])
    
    for i in range(1, N + 1):
        ans = sum_cost - abs(A[i - 1] - A[i]) - abs(A[i] - A[i + 1]) + abs(A[i - 1] - A[i + 1])
        print(ans)


if __name__ == '__main__':
    solve()
