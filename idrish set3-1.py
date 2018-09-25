n, a, d =map(int,input().split())
sum = 0
for i in range(n):
	sum += a + (i * d)
print(sum)
