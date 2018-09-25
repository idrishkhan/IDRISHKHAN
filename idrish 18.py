l,u=map(int,input().split())
for num in range(l+1,u):
	order=len(str(num))
	temp=num
	sum=0
	while (temp>0):
		rem=temp%10
		sum=sum+rem**order
		temp//=10
	if(num==sum):
		print(num)
