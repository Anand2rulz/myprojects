def prime(n,a):
    if n==1:
        return 
    i=2
    while n%i != 0:
        i+=1
    print(i,end=" ")
    prime(n//i,a)
prime(n,2)    



    
    

