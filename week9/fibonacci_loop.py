n = int(input())
a = 1
b = 1
for i in range(n-2):
    a,b = b,a+b
print(b)
