line = input()
numbers = line.split(" ")
n = int(numbers[0])
max = int(numbers[1])

line = input()
lList = line.split(" ")
d, count = 0, 1
for i in range(n):
    d += int(lList[i])
    if d <= max:
        count += 1

print(count)