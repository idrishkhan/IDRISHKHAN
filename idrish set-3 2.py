lst = []
num = int(input())
print(num)
for n in range(num):
    numbers = int(input())
    print(numbers,end=' ')
    lst.append(numbers)
print("\n",max(lst))
