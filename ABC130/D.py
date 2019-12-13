line = input()
numbers = line.split(" ")
n = int(numbers[0])
argMin = int(numbers[1])

line = input()
numbers = line.split(" ")
numberArgs = [0] * len(numbers)
for i in range(len(numbers)):
    numberArgs[i] = int(numbers[i])

count = 0
tmp = 0
j = 0
for i in range(n):
    while tmp < argMin:
        if j == n:
            break
        else:
            tmp += numberArgs[j]
            j += 1
    if tmp < argMin:
        break
    else:
        count += n - j + 1
        tmp -= numberArgs[i]

print(count)
