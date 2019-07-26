n,m=input().split()
n=int(n)
m=int(m)
y=max(n,m)
while(True):
  if(y%n==0 and y%m==0):
    lcm=y
    break
  y=y+1
print(lcm)
  
  
