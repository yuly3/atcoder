from itertools import combinations


def solve():
    N = int(input())
    x = [[] for _ in range(N)]
    y = [[] for _ in range(N)]
    for i in range(N):
        A = int(input())
        xi = [0 for _ in range(A)]
        yi = [0 for _ in range(A)]
        for j in range(A):
            xi[j], yi[j] = map(int, input().split())
            xi[j] -= 1
        x[i] = xi
        y[i] = yi

    ans = 0
    for i in range(1, N+1):
        for honest_peoples in combinations(range(N), i):
            flag = True
            for honest_people in honest_peoples:
                for xij, yij in zip(x[honest_people], y[honest_people]):
                    if xij in honest_peoples and yij == 0 or xij not in honest_peoples and yij == 1:
                        flag = False
                        break
                if not flag:
                    break
            if flag:
                ans = max(ans, i)

    print(ans)


if __name__ == '__main__':
    solve()