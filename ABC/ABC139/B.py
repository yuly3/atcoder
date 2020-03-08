line = list(map(int, input().split()))
A = line[0]
B = line[1]

ans = 0
socket = 1
if B == 1:
  print(ans)
else:
  while True:
    ans += 1
    socket += A - 1
    if socket >= B:
      print(ans)
      break
