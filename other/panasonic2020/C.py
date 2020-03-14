import sys
from decimal import *

rline = sys.stdin.readline


def solve():
    a, b, c = input().split()
    getcontext().prec = 500
    if Decimal.sqrt(Decimal(a)) + Decimal.sqrt(Decimal(b)) < Decimal.sqrt(Decimal(c)):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    solve()
