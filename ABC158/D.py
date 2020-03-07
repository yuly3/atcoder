from collections import deque


def solve():
    S = deque(list(input()))
    Q = int(input())
    state = 0
    for _ in range(Q):
        query = list(input().split())
        if int(query[0]) == 1:
            state = 1 if state == 0 else 0
        else:
            if (state + int(query[1])) % 2 == 1:
                S.appendleft(query[2])
            else:
                S.append(query[2])
    if state == 0:
        print(''.join(S))
    else:
        S.reverse()
        print(''.join(S))


if __name__ == '__main__':
    solve()
