x,y=input().split()
x=int(x)
myl=[]
y=int(y)
ma=max(x,y)
for i in range(1,ma+1):
  if(x%i==0 and y%i==0):
    myl.append(i)
print(max(myl))
