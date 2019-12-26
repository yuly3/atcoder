def solve():
    T = int(input())
    N = int(input())
    A = list(map(int, input().split()))
    M = int(input())
    B = list(map(int, input().split()))
    
    for i in range(M):
        for j in range(len(A)):
            if A[j] <= B[i] <= A[j] + T:
                del A[j]
                break
        else:
            print('no')
            exit()
    print('yes')


if __name__ == '__main__':
    solve()
