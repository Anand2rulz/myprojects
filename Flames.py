#Find the flames of two names
bname=input("enter")
gname=input(("enter"))
l1=list(bname)
l2=list(gname)
for i in range(len(l1)):
    for j in range(len(l2)):
        if l1[i]==l2[j]:
            l1[i]='2'
            l2[j]='2'
print(l1)
print(l2)
x=sum(1 for i in l1 if i!='2')
y=sum(1 for i in l2 if i!='2')
print(x,y)
count=x+y
ans=['f','l','a','m','e','s']
i=0
while len(ans)!=1:
    i=(i+count-1)%len(ans)
    ans.pop(i)
print(ans)    

