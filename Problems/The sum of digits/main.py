num = int(input())
first = num // 100
second = (num - first * 100) // 10
third = (num - first * 100 - second * 10) // 1
print(first + second + third)
