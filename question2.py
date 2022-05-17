y=input('enter a number')
x=int(y)
r=[]
while x>=1:
    r.append(x%2)
    x=x//2
    r.reverse()
for x in r:
    print(x,end='')
        
    
