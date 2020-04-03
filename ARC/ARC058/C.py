import sys

rl = sys.stdin.readline


def solve():
    N, K = map(int, rl().split())
    D = set(map(int, rl().split()))
    
    for ans in range(N, 100000):
        str_ans = str(ans)
        flg = True
        for a in str_ans:
            if int(a) in D:
                flg = False
                break
        if flg:
            print(ans)
            exit()


if __name__ == '__main__':
    solve()
