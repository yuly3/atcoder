from collections import deque


def solve():
    N = int(input())
    S = input()
    ans = deque(S)
    
    l, r = 0, 0
    for i in range(N):
        if S[i] == '(':
            l += 1
        else:
            if 0 < l:
                l -= 1
            else:
                r += 1
    
    for _ in range(l):
        ans.append(')')
    for _ in range(r):
        ans.appendleft('(')
    print(''.join(ans))


if __name__ == '__main__':
    solve()
