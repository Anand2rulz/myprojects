#find the maximum sum in string
s="abcd1234cdef83eg88"
d='1234567890'
sum=0
m=0
for i in s:
    if i in d:
        sum=sum+int(i)
    else:
        m=max(m,sum)
        sum=0
if sum > m :
    print(sum)
else:
    print(m)
        
