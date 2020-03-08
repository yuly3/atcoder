line = input()
numbers = line.split(" ")
w, h, x, y = int(numbers[0]), int(numbers[1]), int(numbers[2]), int(numbers[3])
area = float(w*h/2)
print(str(area), end=" ")
if x == w/2 and y == h/2:
  print("1")
else:
  print("0")
