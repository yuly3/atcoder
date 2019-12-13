forecast = input()
weather = input()

ans = 0
for i in range(3):
  if forecast[i] == weather[i]:
    ans += 1

print(ans)
