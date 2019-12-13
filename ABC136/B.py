number = list(input())

n = len(number) // 2
ans = 0
underNum = ''

if n == 0:
    ans = int(number[0])
else:
    ans = 9
    for i in range(3, len(number) + 1):
        if i == len(number) and i % 2 != 0:
            if int(number[0]) == 1:
                for j in range(1, i):
                    underNum += number[j]
                ans += int(underNum) + 1
            else:
                ans += (int(number[0]) - 1) * 100 ** (i // 2)
                for j in range(1, i):
                    underNum += number[j]
                ans += int(underNum) + 1
        elif i % 2 != 0:
            ans += 9 * 100 ** (i // 2)

print(ans)
