a = [1, 2, 3, 4, 5]
sum = 0
for x in a:
    sum = sum + x
print(sum)
sum = 0
for x in range(101):
    sum = sum + x
print(sum)
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,%s !' % x)
