from collections import deque


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = deque([])
    for i in range(n):
        if i % 2 == 0:
            ans.append(a[i])
        else:
            ans.appendleft(a[i])
    if n % 2 == 1:
        ans.reverse()
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solve()
