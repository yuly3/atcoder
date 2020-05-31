import decimal
import sys
from decimal import Decimal

sys.setrecursionlimit(10 ** 7)
rl = sys.stdin.readline


def solve():
    A, B = rl().split()
    ans = Decimal(A) * Decimal(B)
    ans = ans.quantize(Decimal('0'), rounding=decimal.ROUND_FLOOR)
    print(ans)


if __name__ == '__main__':
    solve()
