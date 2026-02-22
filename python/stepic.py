digit = int(input())
a = digit % 10
b = (digit % 100)//10
c = (digit % 1000)//100
d = digit // 1000

print(a+b+c+d)