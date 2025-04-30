def result(deno,amount):
    deno.sort()
    deno=deno[::-1]
    for coin in deno:
        while amount>=0:
            amount-=int(coin)
            print(coin)

deno=[1,2,5,10,20,50,100,200,500]
n=int(input("enter any amount"))
print(result(deno,n))            
