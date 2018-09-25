ik=int(input())
count=0
for i in range (2,ik):
	if(ik%i==0):
		count = count+1
if(count==0):
	print('Yes')
else:
	print('No')
