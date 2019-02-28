n,k=map(int,input().split())
p=list(map(int,input().split()))
v=list(map(int,input().split()))
m=[]
c=0
for i in range(n):
    x=v[i]/p[i]
    m.append(x)
while k>=0 and len(m)>0:
    mindex=m.index(max(m))
    if k>=p[mindex]:
        c=c+v[mindex]
        k=k-p[mindex]
    p.pop(mindex)
    v.pop(mindex)
    m.pop(mindex)
print(c)
