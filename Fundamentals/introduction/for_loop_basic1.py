for x in range(0, 151):
    print(x)

for x in range(5, 1005, 5):
    print(x)


y = 1
while y < 101:
    print(y)
    y = y + 1
    if y % 5 == 0:
        print("coding")
    if y % 10 == 0:
        print (' Dojo')


min = 0
max = 500000
total = 0
for num in range(min, max+1):
    if(num % 2 != 0):
        print("{0}".format(num))
        total = total + num
print("Sum of Odd Numbers from {0} to {1} = {2}".format(min, max, total))


num = 2018
while num > 0:
    print (num)
    num = num - 4


low= 10
high= 45
mult= 15
for x in range (low, high):
    if x % mult == 0:
        print (x)