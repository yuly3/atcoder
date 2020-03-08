line = list(map(int, input().split()))

ans = 0
if line[0] - line[1] >= line[2]:
  print(ans)
else:
  ans = line[2] - (line[0] - line[1])
  print(ans)
