def solve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    under, over = [], []
    for i in range(N):
        d = A[i] - B[i]
        if d < 0:
            under.append(d)
        elif 0 < d:
            over.append(d)
    over.sort(reverse=True)
    
    ans = len(under)
    lack = -sum(under)
    for i in range(len(over)):
        if lack <= 0:
            break
        lack -= over[i]
        ans += 1
    
    if 0 < lack:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    solve()
