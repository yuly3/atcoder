import sys

def solve():
    N = int(input())
    for i in range(9, 0, -1):
        if N % i == 0 and N / i < 10:
            print('Yes')
            sys.exit()
    print('No')

if __name__ == '__main__':
    solve()
