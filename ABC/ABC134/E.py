from bisect import bisect_left
from collections import deque


def solve():
	N, *A = map(int, open(0).read().split())
	
	top = deque([A[0]])
	for a in A[1:]:
		if top[0] >= a:
			top.appendleft(a)
		else:
			index = bisect_left(top, a)
			top[index-1] = a
	
	print(len(top))


if __name__ == '__main__':
	solve()
