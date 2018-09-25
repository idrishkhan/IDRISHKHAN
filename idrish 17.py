n=int(input())
temp=n
a=0
while(temp!=0):
		rem=temp%10
		a=a+rem*rem*rem
		temp=int(temp/10)
if n==a:
		print('yes')
else :
		print ('no')
