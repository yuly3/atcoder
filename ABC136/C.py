n = int(input())
numbers = list(map(int, input().split()))

def checkCondition():
  for i in range(n-1):
    if numbers[i] > numbers[i+1]:
      if numbers[i] - numbers[i+1] > 1:
        return False
  for i in range(-1, -n, -1):
    sub = numbers[i-1] - numbers[i]
    if sub == 1:
      numbers[i-1] -= 1
    elif sub > 1:
      return False
  return True

if n == 1:
  print('Yes')
else:
  if checkCondition():
    print('Yes')
  else:
    print('No')
